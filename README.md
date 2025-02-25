---

# Bug Bounty Setup Tool

script for bug bounty hunters to install and configure essential tools effortlessly.

---

## Features

- Install and configure essential bug bounty tools.
- Select specific tools or install all tools at once.
- Multi-step installations, including dependencies, compilation, and configuration.

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/MunBytes/BugBountyToolkit.git
   cd BugBountyToolkit
   ```

2. **Make the script executable**:
   ```bash
   chmod +x install.sh
   ```

---


## Example Usage


1. **Run the Setup Script**:
   Execute the shell script as `root` or with `sudo`:
   ```bash
   sudo ./install.sh
   ```

2. **Select Tools to Install**:
   - Enter the number(s) of the tools to install, separated by commas.
   - Or type `all` to install every tool.

---


## Adding New Tools

To add a new tool to the installer:

1. Edit the `tools.json` file.
2. Add a new entry with the following fields:
   ```json
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
   ```
3. Save the file and re-run the script.

---

## Contribution

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch for your changes.
3. Submit a pull request with a detailed description.

---
