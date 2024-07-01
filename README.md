# Templatonator

Templatonator is a Python script designed for Nuke. This tool aims to test and streamline various methods for starting a Nuke script from a template. Beyond simply loading a set of nodes, Templatonator leverages the project settings and color management configurations of the selected template. This ensures consistency and adherence to predefined standards, making it easier to maintain quality and uniformity across different projects.

## Features

- **Template Management**: Load, paste, read, and save Nuke scripts from predefined templates.
- **Flexible Modes**: Choose from different modes of operation like "paste template", "script read", "save to script", "open template", and "copy as text".
- **User Interface**: A custom Nuke panel to select templates and modes, providing an easy-to-use interface for users.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/CequinaVFX/Templatonator.git
2. **Place the script**:
   Copy the script to a location accessible by Nuke.
   Usually ~/.nuke;
3. **Templates Folder**:
    Ensure you have a templates folder in the same directory as the script, containing your .nk template files.

## Modes
- Paste Template: Inserts the template nodes into the current script (this mode doesn't inherit the root node).
- Script Read: Reads the template content into the current script, preserving color management settings.
- Save to Script: Saves the template content to a new script file and opens it.
- Open Template: Directly opens the template file in Nuke and saves it as a new script.
- Copy as Text: Copies the template content as text into a new script file.
