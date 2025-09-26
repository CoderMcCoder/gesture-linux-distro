# Gesture Linux Distribution

A custom Debian-based Linux distribution controlled by hand gestures with a minimalist centered app layout.

## Features

- **Hand Gesture Control**: Navigate and control the system using hand gestures
- **Minimalist Interface**: Clean desktop with centered app icons
- **Custom Desktop Environment**: Lightweight and gesture-optimized
- **Live System**: Bootable ISO for testing and installation

## Project Structure

```
gesture-linux-distro/
├── config/                 # Live-build configuration
├── packages/               # Custom packages
├── scripts/                # Build and setup scripts
├── themes/                 # Custom themes and icons
└── docs/                   # Documentation
```

## Technologies Used

- **Base**: Debian Live-Build
- **Desktop**: Openbox + Custom Launcher
- **Gesture Recognition**: OpenCV + MediaPipe
- **Display**: X11/Wayland
- **Package Management**: APT

## Building

1. Install dependencies: `sudo apt install live-build debootstrap`
2. Configure: `lb config`
3. Build: `sudo lb build`

## Development Status

🚧 **In Development** - Currently setting up the base system and gesture recognition framework.
