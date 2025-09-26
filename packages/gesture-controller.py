#!/usr/bin/env python3
"""
Gesture Controller for Linux Distribution
Hand gesture recognition and system control using OpenCV and MediaPipe
"""

import cv2
import mediapipe as mp
import numpy as np
import subprocess
import threading
import time
import json
import os
from typing import Dict, List, Tuple

class GestureController:
    def __init__(self):
        self.mp_hands = mp.solutions.hands
        self.mp_drawing = mp.solutions.drawing_utils
        self.hands = self.mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=2,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.5
        )
        
        self.cap = cv2.VideoCapture(0)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        
        # Gesture recognition settings
        self.gesture_threshold = 0.8
        self.last_gesture_time = 0
        self.gesture_cooldown = 1.0  # seconds
        
        # System control commands
        self.commands = {
            'swipe_left': 'xdotool key Alt+Left',
            'swipe_right': 'xdotool key Alt+Right',
            'swipe_up': 'xdotool key Alt+Up',
            'swipe_down': 'xdotool key Alt+Down',
            'pinch': 'xdotool key Escape',
            'fist': 'xdotool key Return',
            'peace': 'xdotool key Tab',
            'thumbs_up': 'xdotool key Ctrl+t',
            'thumbs_down': 'xdotool key Ctrl+w'
        }
        
        # Load custom configuration
        self.load_config()
        
    def load_config(self):
        """Load gesture configuration from file"""
        config_path = os.path.expanduser('~/.config/gesture-linux/config.json')
        if os.path.exists(config_path):
            with open(config_path, 'r') as f:
                config = json.load(f)
                self.commands.update(config.get('custom_commands', {}))
    
    def detect_gesture(self, landmarks) -> str:
        """Detect hand gesture from landmarks"""
        if not landmarks:
            return None
            
        # Get finger tip positions
        thumb_tip = landmarks[4]
        index_tip = landmarks[8]
        middle_tip = landmarks[12]
        ring_tip = landmarks[16]
        pinky_tip = landmarks[20]
        
        # Get finger base positions
        thumb_base = landmarks[3]
        index_base = landmarks[5]
        middle_base = landmarks[9]
        ring_base = landmarks[13]
        pinky_base = landmarks[17]
        
        # Calculate finger states (extended or not)
        fingers = []
        
        # Thumb (compare x-coordinate)
        fingers.append(thumb_tip.x > thumb_base.x)
        
        # Other fingers (compare y-coordinate)
        fingers.extend([
            index_tip.y < index_base.y,
            middle_tip.y < middle_base.y,
            ring_tip.y < ring_base.y,
            pinky_tip.y < pinky_base.y
        ])
        
        # Gesture recognition
        if sum(fingers) == 0:
            return 'fist'
        elif sum(fingers) == 2 and fingers[1] and fingers[2]:
            return 'peace'
        elif sum(fingers) == 1 and fingers[0]:
            return 'thumbs_up'
        elif sum(fingers) == 4 and not fingers[0]:
            return 'four_fingers'
        elif sum(fingers) == 5:
            return 'open_hand'
        
        return None
    
    def execute_command(self, gesture: str):
        """Execute system command based on gesture"""
        if gesture in self.commands:
            try:
                subprocess.run(self.commands[gesture], shell=True, check=True)
                print(f"Executed: {gesture} -> {self.commands[gesture]}")
            except subprocess.CalledProcessError as e:
                print(f"Error executing command: {e}")
    
    def run(self):
        """Main gesture recognition loop"""
        print("🎯 Gesture Controller started!")
        print("Available gestures:")
        for gesture, command in self.commands.items():
            print(f"  {gesture}: {command}")
        print("\nPress 'q' to quit")
        
        while True:
            ret, frame = self.cap.read()
            if not ret:
                break
                
            # Flip frame horizontally for mirror effect
            frame = cv2.flip(frame, 1)
            
            # Convert BGR to RGB
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            
            # Process frame
            results = self.hands.process(rgb_frame)
            
            # Draw hand landmarks
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    self.mp_drawing.draw_landmarks(
                        frame, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)
                    
                    # Detect gesture
                    landmarks = [(lm.x, lm.y) for lm in hand_landmarks.landmark]
                    gesture = self.detect_gesture(landmarks)
                    
                    if gesture and time.time() - self.last_gesture_time > self.gesture_cooldown:
                        self.execute_command(gesture)
                        self.last_gesture_time = time.time()
                        
                        # Visual feedback
                        cv2.putText(frame, f"Gesture: {gesture}", 
                                  (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            
            # Display frame
            cv2.imshow('Gesture Controller', frame)
            
            # Exit on 'q' key
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        
        self.cleanup()
    
    def cleanup(self):
        """Clean up resources"""
        self.cap.release()
        cv2.destroyAllWindows()
        print("👋 Gesture Controller stopped")

def main():
    """Main entry point"""
    try:
        controller = GestureController()
        controller.run()
    except KeyboardInterrupt:
        print("\n👋 Gesture Controller interrupted by user")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
