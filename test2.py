import subprocess
import platform
import os
from pathlib import Path
import time

# Detect platform and set binary path
IS_WINDOWS = platform.system() == "Windows"

# Set this to the directory where xvf_host(.exe) is stored
XVF_TOOL_DIR = Path(__file__).parent

xvf_host_binary = str(XVF_TOOL_DIR / ("xvf_host.exe" if IS_WINDOWS else "xvf_host"))

# Optional: Ensure Unix binary is executable
if not IS_WINDOWS:
    subprocess.run(["chmod", "+x", xvf_host_binary])

def run_xvf_command(command: str, *args):
    """Runs a command using the xvf_host(.exe) binary"""
    cmd = [xvf_host_binary] + command.split() + [str(arg) for arg in args]
    print(f"> Running: {' '.join(cmd)}")
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        print(result.stdout)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print("❌ Error:", e.stderr)
        return None

# ----------- USAGE EXAMPLES -------------

if __name__ == "__main__":
    # Check version
    run_xvf_command("VERSION")
    time.sleep(0.005)
    # LED breath mode: orange color
    run_xvf_command("led_effect", 1)
    time.sleep(0.005)
    run_xvf_command("led_color", "0xff8800")
    time.sleep(0.005)
    run_xvf_command("led_speed", 1)
    time.sleep(0.005)
    run_xvf_command("led_brightness", 255)
    time.sleep(0.005)

    # Save config
    #run_xvf_command("save_configuration", 1)
    #time.sleep(0.005)

    # Uncomment to clear config
    run_xvf_command("clear_configuration", 1)
    time.sleep(0.005)
