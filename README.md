
# 📦 Cross-Platform Python Wrapper for ReSpeaker XVF3800

## 🔧 Overview
This guide explains how to **control the ReSpeaker XVF3800** using a **cross-platform Python script** via `xvf_host(.exe)` and its required dynamic libraries. It supports:

✅ Windows  
✅ Linux  
✅ macOS  
✅ Raspberry Pi OS

It allows you to control LED effects, brightness, DoA color, and manage configuration (save/clear).

---

## 📁 Folder Structure

Your GitHub repo should contain the following files:

```
reSpeakerXVF/
├── xvf_host.exe              # Windows binary
├── xvf_host                  # Linux/macOS/RPi binary (make it executable)
├── libcommand_map.dll        # Windows
├── libdevice_usb.dll         # Windows
├── libcommand_map.dylib      # macOS
├── libdevice_usb.dylib       # macOS
├── libusb-1.0.0.dylib        # macOS
├── test.py                   # Cross-platform Python controller
```

---

## 🐍 Getting Started with Python

### 📦 Requirements

- Python 3.7+
- No external Python libraries required (uses `subprocess`)
- Make sure the required `.dll`/`.dylib` files are in the **same folder** as the `xvf_host(.exe)` binary

---

### 🚀 Running the Python Script

1. **Clone the repository**
```bash
git clone https://github.com/KasunThushara/reSpeakerXVF.git
cd reSpeakerXVF
```

2. **Make Linux/macOS binary executable**
```bash
chmod +x xvf_host
```

3. **Run the Python script**
```bash
python test.py
```

This will:
- Print the firmware version
- Set the LED ring to breath mode with an orange color
- Set LED speed and brightness
- Save the configuration to flash

---

### 🧪 Example Output
```
> Running: ./xvf_host VERSION
Device (USB)::device_init() -- Found device VID: 10374 PID: 26 interface: 3
VERSION 2 0 2
```

---

## 🧠 test.py Code Summary

The script:
- Automatically detects your OS (Windows/Linux/macOS)
- Executes the `xvf_host` command with the correct binary
- Supports any XVF3800 command like `led_effect`, `led_color`, `save_configuration`, etc.

### 🧩 Example Custom Commands
```python
run_xvf_command("led_doa_color", "0x0000ff", "0xff0000")
run_xvf_command("clear_configuration", 1)  # Then manually reboot
```

---

## 💡 Notes

- For Windows: ensure `.dll` files are in the same folder as `xvf_host.exe`
- For macOS: ensure `.dylib` files are present (you may need to allow unsigned libraries via `System Settings > Security`)
- For Linux: may require installing `libusb-1.0` (`sudo apt install libusb-1.0-0-dev`)

---
