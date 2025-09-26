# Gesture Linux Distribution - Build Guide

## 🚀 Building Your Gesture-Controlled Linux Distribution

Since Docker is having issues, here are several ways to build your custom Linux distribution:

## Method 1: Using a Debian/Ubuntu Virtual Machine (Recommended)

### Step 1: Set up a Debian/Ubuntu VM
1. **Download Debian 12 (Bookworm)** from [debian.org](https://www.debian.org/distrib/)
2. **Create a VM** with at least:
   - 4GB RAM
   - 20GB disk space
   - 2 CPU cores

### Step 2: Transfer Files to VM
```bash
# Copy the entire gesture-linux-distro folder to your VM
scp -r gesture-linux-distro/ user@vm-ip:/home/user/
```

### Step 3: Build in VM
```bash
# SSH into your VM or work directly in it
ssh user@vm-ip

# Navigate to the project
cd gesture-linux-distro

# Run the setup script
sudo ./scripts/setup.sh

# Build the distribution
sudo ./scripts/build.sh
```

## Method 2: Using GitHub Codespaces

### Step 1: Push to GitHub
```bash
# Initialize git repository
git init
git add .
git commit -m "Initial commit: Gesture Linux Distribution"

# Create GitHub repository and push
git remote add origin https://github.com/yourusername/gesture-linux-distro.git
git push -u origin main
```

### Step 2: Create Codespace
1. Go to your GitHub repository
2. Click "Code" → "Codespaces" → "Create codespace"
3. Wait for the environment to load

### Step 3: Build in Codespace
```bash
# In the Codespace terminal
sudo ./scripts/setup.sh
sudo ./scripts/build.sh
```

## Method 3: Using WSL2 (Windows) or Linux Subsystem

### For Windows Users:
```bash
# Install WSL2 with Ubuntu
wsl --install -d Ubuntu

# In WSL2 Ubuntu
sudo apt update
sudo apt install live-build debootstrap
cd /mnt/c/path/to/gesture-linux-distro
sudo ./scripts/build.sh
```

## Method 4: Manual Build Process

If the automated scripts don't work, here's the manual process:

### Step 1: Install Dependencies
```bash
sudo apt update
sudo apt install live-build debootstrap build-essential devscripts dh-make
sudo apt install python3 python3-pip python3-opencv python3-numpy python3-tk
sudo apt install xorg openbox lightdm nitrogen feh tint2 conky lxappearance
sudo apt install firefox-esr thunar geany xterm htop neofetch vim nano
sudo apt install xdotool wmctrl xinput x11-xserver-utils arandr
sudo apt install alsa-utils pulseaudio vlc network-manager
sudo apt install arc-theme papirus-icon-theme

# Install MediaPipe
pip3 install --break-system-packages mediapipe
```

### Step 2: Initialize Live-Build
```bash
# Clean any previous builds
sudo lb clean --purge

# Initialize configuration
lb config \
    --distribution bookworm \
    --archive-areas "main contrib non-free" \
    --bootloader syslinux \
    --binary-images iso-hybrid \
    --cache true \
    --cache-packages true \
    --cache-stages true \
    --debian-installer live \
    --debian-installer-gui false \
    --iso-application "Gesture Linux Distribution" \
    --iso-preparer "Gesture Linux Team" \
    --iso-publisher "Gesture Linux Team" \
    --iso-volume "Gesture Linux" \
    --packages-lists "gesture-linux" \
    --hooks "0100-install-gesture-apps" \
    --includes "etc/openbox/rc.xml"
```

### Step 3: Copy Custom Files
```bash
# Copy packages to build directory
sudo cp -r packages/ /build/
```

### Step 4: Build the ISO
```bash
# Build the distribution (this takes 30-60 minutes)
sudo lb build
```

### Step 5: Check Results
```bash
# The ISO should be created as binary.iso
ls -la binary.iso
file binary.iso
```

## Method 5: Using Cloud Build Services

### GitHub Actions (Free)
Create `.github/workflows/build.yml`:
```yaml
name: Build Gesture Linux Distribution

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Install dependencies
      run: |
        sudo apt update
        sudo apt install live-build debootstrap build-essential devscripts dh-make
        sudo apt install python3 python3-pip python3-opencv python3-numpy python3-tk
        sudo apt install xorg openbox lightdm nitrogen feh tint2 conky lxappearance
        sudo apt install firefox-esr thunar geany xterm htop neofetch vim nano
        sudo apt install xdotool wmctrl xinput x11-xserver-utils arandr
        sudo apt install alsa-utils pulseaudio vlc network-manager
        sudo apt install arc-theme papirus-icon-theme
        pip3 install --break-system-packages mediapipe
    
    - name: Build ISO
      run: |
        sudo ./scripts/build.sh
    
    - name: Upload ISO
      uses: actions/upload-artifact@v3
      with:
        name: gesture-linux-iso
        path: binary.iso
```

## Troubleshooting

### Common Issues:

1. **Permission Denied**: Make sure to run with `sudo`
2. **Package Not Found**: Update package lists with `sudo apt update`
3. **Build Fails**: Check logs in `/var/log/live-build/`
4. **ISO Too Large**: Remove unnecessary packages from package list
5. **MediaPipe Issues**: Use `--break-system-packages` flag

### Build Logs:
```bash
# Check build logs
sudo tail -f /var/log/live-build/live-build.log

# Check for errors
sudo grep -i error /var/log/live-build/live-build.log
```

## Expected Results

After successful build, you should have:
- `binary.iso` - Your bootable Gesture Linux distribution
- File size: ~2-4GB
- Bootable on any x86_64 system
- Includes gesture control and centered launcher

## Testing Your ISO

1. **Virtual Machine**: Boot the ISO in VirtualBox/VMware
2. **USB Drive**: Use tools like Rufus or Balena Etcher
3. **Live Boot**: Boot directly from ISO on a test machine

## Next Steps

Once you have your ISO:
1. Test gesture recognition with a webcam
2. Verify the centered launcher works
3. Customize applications and gestures
4. Share your creation!

---

**Need Help?** Check the troubleshooting section or create an issue in the project repository.
