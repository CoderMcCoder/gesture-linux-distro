#!/bin/bash

# Gesture Linux Distribution Build Script
# This script builds the custom Debian-based distribution

set -e

echo "🚀 Building Gesture Linux Distribution..."

# Check if we're in the right directory
if [ ! -f "config/package-lists/gesture-linux.list.chroot" ]; then
    echo "❌ Please run this script from the gesture-linux-distro directory"
    exit 1
fi

# Check if live-build is installed
if ! command -v lb &> /dev/null; then
    echo "❌ live-build is not installed. Please run ./scripts/setup.sh first"
    exit 1
fi

# Clean previous builds
echo "🧹 Cleaning previous builds..."
sudo lb clean --purge

# Initialize configuration
echo "⚙️ Initializing live-build configuration..."
lb config \
    --distribution bookworm \
    --archive-areas "main contrib non-free" \
    --bootloader syslinux \
    --binary-images iso-hybrid \
    --architecture arm64 \
    --cache true \
    --cache-packages true \
    --cache-stages true \
    --debian-installer live \
    --debian-installer-gui false \
    --iso-application "Gesture Linux Distribution" \
    --iso-preparer "Gesture Linux Team" \
    --iso-publisher "Gesture Linux Team" \
    --iso-volume "Gesture Linux"

# Copy custom packages to build directory
echo "📦 Copying custom packages..."
sudo cp -r packages/ /build/

# Build the distribution
echo "🔨 Building the distribution (this may take a while)..."
sudo lb build

# Check if build was successful
if [ -f "binary.iso" ]; then
    echo "✅ Build successful!"
    echo "📁 ISO file: $(pwd)/binary.iso"
    echo "📊 File size: $(du -h binary.iso | cut -f1)"
    echo ""
    echo "🎯 Next steps:"
    echo "1. Test the ISO in a virtual machine"
    echo "2. Burn to USB or DVD for installation"
    echo "3. Enjoy your gesture-controlled Linux distribution!"
else
    echo "❌ Build failed. Check the output above for errors."
    exit 1
fi
