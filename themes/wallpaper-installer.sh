#!/bin/bash

# Wallpaper installer for Gesture Linux Distribution
# Sets up beautiful wallpapers optimized for the centered launcher

set -e

echo "🎨 Installing wallpapers for Gesture Linux Distribution..."

# Create wallpaper directory
WALLPAPER_DIR="/usr/share/backgrounds/gesture-linux"
sudo mkdir -p "$WALLPAPER_DIR"

# Create a simple gradient wallpaper using ImageMagick
echo "🖼️ Creating default wallpapers..."

# Dark gradient wallpaper (default)
sudo convert -size 1920x1080 gradient:'#1a1a1a-#2d2d2d' "$WALLPAPER_DIR/dark-gradient.jpg"

# Light gradient wallpaper
sudo convert -size 1920x1080 gradient:'#f0f0f0-#e0e0e0' "$WALLPAPER_DIR/light-gradient.jpg"

# Blue gradient wallpaper
sudo convert -size 1920x1080 gradient:'#1e3c72-#2a5298' "$WALLPAPER_DIR/blue-gradient.jpg"

# Purple gradient wallpaper
sudo convert -size 1920x1080 gradient:'#667eea-#764ba2' "$WALLPAPER_DIR/purple-gradient.jpg"

# Create wallpaper configuration
sudo tee /etc/gesture-linux/wallpaper.conf > /dev/null << EOF
# Gesture Linux Wallpaper Configuration
DEFAULT_WALLPAPER="$WALLPAPER_DIR/dark-gradient.jpg"
WALLPAPER_DIR="$WALLPAPER_DIR"
EOF

# Set default wallpaper
sudo nitrogen --set-zoom-fill "$WALLPAPER_DIR/dark-gradient.jpg"

echo "✅ Wallpapers installed successfully!"
echo "📁 Wallpaper directory: $WALLPAPER_DIR"
echo "🎨 Available wallpapers:"
ls -la "$WALLPAPER_DIR"
