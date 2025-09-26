# Gesture Linux Distribution - User Guide

## Welcome to Gesture Linux! 🎯

Gesture Linux is a custom Debian-based distribution designed to be controlled primarily through hand gestures, featuring a minimalist centered app launcher interface.

## Getting Started

### System Requirements

- **CPU**: x86_64 processor
- **RAM**: Minimum 2GB, Recommended 4GB+
- **Storage**: 10GB free space
- **Camera**: USB webcam for gesture recognition
- **Graphics**: Any graphics card with X11 support

### First Boot

1. **Boot from ISO**: Insert the Gesture Linux ISO and boot your system
2. **Live Mode**: The system will start in live mode - no installation required
3. **Installation**: Use the installer to install to your hard drive

## Gesture Controls

### Supported Gestures

| Gesture | Action | Description |
|---------|--------|-------------|
| 👊 **Fist** | Enter/Return | Confirm selection, press Enter |
| ✌️ **Peace Sign** | Tab | Navigate between elements |
| 👍 **Thumbs Up** | New Tab | Open new browser tab |
| 👎 **Thumbs Down** | Close Tab | Close current browser tab |
| 👈 **Swipe Left** | Alt+Left | Go back |
| 👉 **Swipe Right** | Alt+Right | Go forward |
| 👆 **Swipe Up** | Alt+Up | Scroll up |
| 👇 **Swipe Down** | Alt+Down | Scroll down |
| 🤏 **Pinch** | Escape | Close dialog, cancel action |

### Gesture Tips

- **Hold gestures steady** for 1 second for recognition
- **Ensure good lighting** for better gesture detection
- **Keep hands visible** to the camera
- **Use one hand at a time** for best results

## Interface Overview

### Centered Launcher

The main interface features a clean, centered app launcher with:

- **App Grid**: 3-column layout with your main applications
- **Status Bar**: Shows system status and current time
- **Full-screen Mode**: Distraction-free interface
- **Gesture Feedback**: Visual confirmation of recognized gestures

### Default Applications

- 🌐 **Web Browser** (Firefox)
- 📁 **File Manager** (Thunar)
- 📝 **Text Editor** (Geany)
- 💻 **Terminal** (XTerm)
- ⚙️ **Settings** (LXAppearance)
- 📊 **System Monitor** (Htop)

## Customization

### Adding Applications

1. Edit `/home/user/.config/gesture-linux/apps.json`
2. Add your application:
```json
{
    "name": "My App",
    "command": "my-app-command",
    "icon": "🎯",
    "description": "My custom application"
}
```
3. Restart the launcher

### Customizing Gestures

1. Edit `/home/user/.config/gesture-linux/config.json`
2. Modify gesture commands:
```json
{
    "custom_commands": {
        "fist": "xdotool key Return",
        "peace": "xdotool key Tab"
    }
}
```
3. Restart the gesture controller

### Changing Wallpapers

1. Place wallpaper images in `/usr/share/backgrounds/gesture-linux/`
2. Use Nitrogen to set wallpaper:
```bash
nitrogen /usr/share/backgrounds/gesture-linux/
```

## Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| `Alt+F1` | Open Centered Launcher |
| `Alt+F2` | Open File Manager |
| `Alt+F3` | Open Web Browser |
| `Alt+F4` | Open Terminal |
| `Alt+Tab` | Switch between windows |
| `Alt+F4` | Close current window |
| `Escape` | Close launcher |

## Troubleshooting

### Gesture Recognition Issues

**Problem**: Gestures not being recognized
**Solutions**:
- Check camera permissions
- Ensure good lighting
- Restart gesture controller: `sudo systemctl restart gesture-controller`
- Check camera with: `lsusb` or `v4l2-ctl --list-devices`

**Problem**: Gestures too sensitive/not sensitive enough
**Solutions**:
- Adjust threshold in config: `gesture_threshold` (0.5-0.9)
- Adjust cooldown: `gesture_cooldown` (0.5-2.0 seconds)

### Performance Issues

**Problem**: System running slowly
**Solutions**:
- Close unnecessary applications
- Check system resources with Htop
- Reduce gesture recognition sensitivity

### Application Issues

**Problem**: Applications not launching
**Solutions**:
- Check if application is installed: `which application-name`
- Check application permissions
- Try launching from terminal for error messages

## Advanced Usage

### Command Line Access

Access terminal through:
- Alt+F4 keyboard shortcut
- Gesture launcher → Terminal
- Right-click desktop → Terminal

### System Administration

- **Package Management**: Use `apt` for installing packages
- **Service Management**: Use `systemctl` for managing services
- **User Management**: Use `useradd`, `usermod`, `userdel`

### Development

Gesture Linux includes development tools:
- Build tools: `build-essential`
- Package creation: `devscripts`, `dh-make`
- Version control: `git`

## Support

### Getting Help

- **Documentation**: Check `/usr/share/doc/gesture-linux/`
- **Logs**: Check system logs with `journalctl`
- **Community**: Join our community forums
- **Issues**: Report bugs on our GitHub repository

### Contributing

We welcome contributions! Areas where you can help:
- New gesture recognition algorithms
- Additional applications
- Theme and wallpaper creation
- Documentation improvements
- Bug fixes and testing

## License

Gesture Linux Distribution is released under the GNU General Public License v3.0.

---

**Enjoy your gesture-controlled Linux experience!** 🎉
