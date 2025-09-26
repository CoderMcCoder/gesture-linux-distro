#!/bin/bash

# Gesture Linux Distribution Setup Script for macOS
# This script sets up the development environment using Docker

set -e

echo "🚀 Setting up Gesture Linux Distribution development environment on macOS..."

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "❌ Docker is required but not installed."
    echo "Please install Docker Desktop from: https://www.docker.com/products/docker-desktop"
    exit 1
fi

# Check if Homebrew is installed
if ! command -v brew &> /dev/null; then
    echo "❌ Homebrew is required but not installed."
    echo "Please install Homebrew from: https://brew.sh"
    exit 1
fi

# Install Docker if not running
if ! docker info &> /dev/null; then
    echo "🐳 Starting Docker..."
    open -a Docker
    echo "Please wait for Docker to start, then press Enter to continue..."
    read
fi

# Create Dockerfile for building
echo "📦 Creating Docker build environment..."
cat > Dockerfile << 'EOF'
FROM debian:bookworm-slim

# Install build dependencies
RUN apt-get update && apt-get install -y \
    live-build \
    debootstrap \
    build-essential \
    devscripts \
    dh-make \
    git \
    curl \
    wget \
    python3 \
    python3-pip \
    python3-opencv \
    python3-numpy \
    python3-mediapipe \
    python3-tkinter \
    python3-pyqt5 \
    libopencv-dev \
    libgtk-3-dev \
    xorg \
    openbox \
    lightdm \
    nitrogen \
    feh \
    tint2 \
    conky \
    lxappearance \
    gtk2-engines-murrine \
    gtk3-engines-breeze \
    firefox-esr \
    thunar \
    geany \
    xterm \
    htop \
    neofetch \
    vim \
    nano \
    xdotool \
    wmctrl \
    xinput \
    xrandr \
    arandr \
    alsa-utils \
    pulseaudio \
    vlc \
    network-manager \
    wpasupplicant \
    wireless-tools \
    arc-theme \
    papirus-icon-theme \
    unzip \
    zip \
    tar \
    gzip \
    rsync \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /build

# Copy project files
COPY . .

# Make scripts executable
RUN chmod +x scripts/*.sh
RUN chmod +x themes/*.sh
RUN chmod +x config/hooks/*.sh

CMD ["/bin/bash"]
EOF

echo "✅ Docker environment ready!"
echo ""
echo "Next steps:"
echo "1. Build Docker image: docker build -t gesture-linux-builder ."
echo "2. Run build: docker run -it --privileged gesture-linux-builder"
echo "3. Inside container, run: ./scripts/build.sh"
