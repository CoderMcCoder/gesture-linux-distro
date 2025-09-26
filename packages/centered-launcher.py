#!/usr/bin/env python3
"""
Centered Launcher for Gesture Linux Distribution
A minimalist launcher with centered app icons optimized for gesture control
"""

import tkinter as tk
from tkinter import ttk
import subprocess
import json
import os
from typing import Dict, List

class CenteredLauncher:
    def __init__(self):
        self.root = tk.Tk()
        self.setup_window()
        self.load_apps()
        self.create_interface()
        
    def setup_window(self):
        """Configure the main window"""
        self.root.title("Gesture Linux Launcher")
        self.root.attributes('-fullscreen', True)
        self.root.configure(bg='#1a1a1a')
        
        # Make window stay on top
        self.root.attributes('-topmost', True)
        
        # Bind escape key to close
        self.root.bind('<Escape>', lambda e: self.root.quit())
        
        # Center the window
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
    
    def load_apps(self):
        """Load application configuration"""
        self.apps = [
            {
                'name': 'Web Browser',
                'command': 'firefox',
                'icon': '🌐',
                'description': 'Browse the internet'
            },
            {
                'name': 'File Manager',
                'command': 'thunar',
                'icon': '📁',
                'description': 'Manage files and folders'
            },
            {
                'name': 'Text Editor',
                'command': 'geany',
                'icon': '📝',
                'description': 'Edit text files'
            },
            {
                'name': 'Terminal',
                'command': 'xterm',
                'icon': '💻',
                'description': 'Command line interface'
            },
            {
                'name': 'Settings',
                'command': 'lxappearance',
                'icon': '⚙️',
                'description': 'System settings'
            },
            {
                'name': 'System Monitor',
                'command': 'htop',
                'icon': '📊',
                'description': 'Monitor system resources'
            }
        ]
        
        # Load custom apps from config
        config_path = os.path.expanduser('~/.config/gesture-linux/apps.json')
        if os.path.exists(config_path):
            try:
                with open(config_path, 'r') as f:
                    custom_apps = json.load(f)
                    self.apps.extend(custom_apps)
            except json.JSONDecodeError:
                print("Warning: Invalid apps.json format")
    
    def create_interface(self):
        """Create the main interface"""
        # Main container
        main_frame = tk.Frame(self.root, bg='#1a1a1a')
        main_frame.pack(expand=True, fill='both')
        
        # Title
        title_label = tk.Label(
            main_frame,
            text="Gesture Linux",
            font=('Arial', 24, 'bold'),
            fg='#ffffff',
            bg='#1a1a1a'
        )
        title_label.pack(pady=(50, 20))
        
        # Apps grid
        self.create_apps_grid(main_frame)
        
        # Status bar
        self.create_status_bar(main_frame)
    
    def create_apps_grid(self, parent):
        """Create the centered apps grid"""
        # Apps container
        apps_frame = tk.Frame(parent, bg='#1a1a1a')
        apps_frame.pack(expand=True, fill='both', padx=50, pady=20)
        
        # Calculate grid dimensions
        num_apps = len(self.apps)
        cols = 3  # Fixed number of columns
        rows = (num_apps + cols - 1) // cols
        
        # Create app buttons
        self.app_buttons = []
        for i, app in enumerate(self.apps):
            row = i // cols
            col = i % cols
            
            # App button frame
            app_frame = tk.Frame(apps_frame, bg='#1a1a1a')
            app_frame.grid(row=row, column=col, padx=20, pady=20, sticky='nsew')
            
            # Configure grid weights
            apps_frame.grid_rowconfigure(row, weight=1)
            apps_frame.grid_columnconfigure(col, weight=1)
            
            # App button
            button = tk.Button(
                app_frame,
                text=f"{app['icon']}\n{app['name']}",
                font=('Arial', 12),
                bg='#2d2d2d',
                fg='#ffffff',
                activebackground='#404040',
                activeforeground='#ffffff',
                relief='flat',
                bd=0,
                padx=20,
                pady=20,
                cursor='hand2',
                command=lambda cmd=app['command']: self.launch_app(cmd)
            )
            button.pack(expand=True, fill='both')
            
            # Add hover effects
            button.bind('<Enter>', lambda e, btn=button: btn.configure(bg='#404040'))
            button.bind('<Leave>', lambda e, btn=button: btn.configure(bg='#2d2d2d'))
            
            self.app_buttons.append(button)
    
    def create_status_bar(self, parent):
        """Create status bar at bottom"""
        status_frame = tk.Frame(parent, bg='#1a1a1a', height=50)
        status_frame.pack(side='bottom', fill='x', padx=20, pady=10)
        status_frame.pack_propagate(False)
        
        # Status text
        self.status_label = tk.Label(
            status_frame,
            text="Ready • Press ESC to close • Gesture control active",
            font=('Arial', 10),
            fg='#888888',
            bg='#1a1a1a'
        )
        self.status_label.pack(side='left')
        
        # Time display
        self.time_label = tk.Label(
            status_frame,
            font=('Arial', 10),
            fg='#888888',
            bg='#1a1a1a'
        )
        self.time_label.pack(side='right')
        
        # Update time
        self.update_time()
    
    def update_time(self):
        """Update time display"""
        import datetime
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        self.time_label.configure(text=current_time)
        self.root.after(1000, self.update_time)
    
    def launch_app(self, command: str):
        """Launch an application"""
        try:
            # Launch in background
            subprocess.Popen(command, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            self.status_label.configure(text=f"Launched: {command}")
            
            # Reset status after 2 seconds
            self.root.after(2000, lambda: self.status_label.configure(
                text="Ready • Press ESC to close • Gesture control active"
            ))
            
        except Exception as e:
            self.status_label.configure(text=f"Error launching {command}: {e}")
    
    def run(self):
        """Start the launcher"""
        self.root.mainloop()

def main():
    """Main entry point"""
    try:
        launcher = CenteredLauncher()
        launcher.run()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
