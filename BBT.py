import os
import platform
import subprocess
import json
import sys

CONFIG_FILE = "tools.json"

# config file structure
"""
{
    "name": "ToolName",
    "description": "Description of the tool.",
    "check_command": "Command to check if the tool is installed.",
    "installation": {
        "linux": ["List of commands to install the tool"]
    },
    "post_install": {
        "linux": ["List of commands to run after installation (optional)"]
    }
}

"""



def load_config():
    if not os.path.exists(CONFIG_FILE):
        print(f"[ERROR] Configuration file '{CONFIG_FILE}' not found!")
        sys.exit(1)
    with open(CONFIG_FILE, 'r') as f:
        return json.load(f)


def run_command(command):
    try:
        print(f"[INFO] Running: {command}")
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] Command failed: {command}\n{e}")
        sys.exit(1)

def is_tool_installed(check_command):
    try:
        subprocess.run(check_command, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
        return True
    except subprocess.CalledProcessError:
        return False

def install_tool(tool):
    print(f"\n[INFO] Checking if {tool['name']} is already installed...")
    if 'check_command' in tool and is_tool_installed(tool['check_command']):
        print(f"[INFO] {tool['name']} is already installed. Skipping installation.")
        return

    print(f"[INFO] Installing {tool['name']}...")
    os_type = platform.system().lower()
    if os_type not in tool['installation']:
        print(f"[ERROR] OS not supported for {tool['name']}")
        return

    steps = tool['installation'][os_type]
    for step in steps:
        run_command(step)

    print(f"[SUCCESS] {tool['name']} installed successfully!")


    # Post-installation steps
    if 'post_install' in tool and os_type in tool['post_install']:
        print(f"[INFO] Running post-installation steps for {tool['name']}...")
        for step in tool['post_install'][os_type]:
            run_command(step)
        print(f"[SUCCESS] Post-installation completed for {tool['name']}!")




def list_tools(tools):
    print("\nAvailable tools:")
    for idx, tool in enumerate(tools, 1):
        print(f"{idx}. {tool['name']} - {tool['description']}")


def main():
    tools = load_config()
    list_tools(tools)
    choice = input("\nEnter the number(s) of the tool(s) to install (comma-separated), or 'all' for everything: ").strip()
    if not choice:
        print(f"Quitting...\n")
        sys.exit(0)

    if choice.lower() == 'all':
        for tool in tools:
            install_tool(tool)
    else:
        selected_tools = []
        for item in choice.split(','):
            item = item.strip()
            index = int(item) - 1
            if 0 <= index < len(tools):
                selected_tools.append(tools[index])
            else:
                print(f"[ERROR] Invalid tool number: {item}")

        if selected_tools:
            for tool in selected_tools:
                install_tool(tool)
        else:
            print("[ERROR] No valid tools selected. Exiting.")
            sys.exit(1)






if __name__ == "__main__":
    main()
