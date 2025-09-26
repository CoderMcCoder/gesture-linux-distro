#!/bin/bash

# Gesture Linux Distribution Setup Script
# This script sets up the development environment for building the custom distro

set -e

echo "🚀 Setting up Gesture Linux Distribution development environment..."

# Check if running on Debian/Ubuntu
if ! command -v apt &> /dev/null; then
    echo "❌ This script requires apt package manager (Debian/Ubuntu)"
    exit 1
fi

# Update package lists
echo "📦 Updating package lists..."
sudo apt update

# Install essential build tools
echo "🔧 Installing build tools..."
sudo apt install -y \
    live-build \
    debootstrap \
    build-essential \
    devscripts \
    dh-make \
    git \
    curl \
    wget

# Install gesture recognition dependencies
echo "👋 Installing gesture recognition dependencies..."
sudo apt install -y \
    python3 \
    python3-pip \
    python3-opencv \
    python3-numpy \
    python3-mediapipe \
    python3-tkinter \
    python3-pyqt5 \
    libopencv-dev \
    libgtk-3-dev

# Install desktop environment dependencies
echo "🖥️ Installing desktop environment dependencies..."
sudo apt install -y \
    xorg \
    openbox \
    lightdm \
    nitrogen \
    feh \
    tint2 \
    conky \
    lxappearance \
    gtk2-engines-murrine \
    gtk3-engines-breeze

# Install additional useful packages
echo "📱 Installing additional packages..."
sudo apt install -y \
    firefox-esr \
    thunar \
    geany \
    htop \
    neofetch \
    vim \
    nano

echo "✅ Setup complete! You can now run 'lb config' to initialize the live-build configuration."
echo ""
echo "Next steps:"
echo "1. Run: lb config"
echo "2. Customize config/ directory"
echo "3. Run: sudo lb build"
