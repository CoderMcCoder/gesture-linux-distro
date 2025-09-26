FROM --platform=linux/arm64 debian:bookworm-slim

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
    python3-tk \
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
    x11-xserver-utils \
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

# Install MediaPipe via pip with system packages override
RUN pip3 install --break-system-packages mediapipe

# Set working directory
WORKDIR /build

# Copy project files
COPY . .

# Make scripts executable
RUN chmod +x scripts/*.sh
RUN chmod +x themes/*.sh
RUN find config/hooks -name "*.sh" -exec chmod +x {} \; 2>/dev/null || true

CMD ["/bin/bash"]
