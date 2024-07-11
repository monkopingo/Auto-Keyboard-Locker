---

# Keyboard Blocker ⌨️🚫

Keyboard Blocker is a simple utility to block your keyboard after a period of inactivity or manually via the system tray. It can be useful to prevent unwanted key presses from pets, such as cats walking on your keyboard, or to ensure no accidental key presses when you're away from your computer.

## Features ✨

- 🕒 Automatically blocks the keyboard after 12 minutes of inactivity.
- 🖱️ Manually block and unblock the keyboard through the system tray icon.
- ⚠️ Displays a system message when attempting to use a blocked keyboard.
- 📂 Easily accessible system tray icon with options to lock, unlock, and exit the application.

## Installation 🛠️

1. Clone the repository or download the source code:

   ```sh
   git clone https://github.com/yourusername/keyboard-blocker.git
   cd keyboard-blocker
   ```

2. Install the required Python packages:

   ```sh
   pip install pystray keyboard pillow
   ```

3. Compile the script into a single executable using PyInstaller:

   ```sh
   pyinstaller --onefile blocker.py
   ```

   This will create a standalone executable in the `dist` directory.

## Usage 🚀

1. Run the executable or the Python script:

   ```sh
   python blocker.py
   ```

   Or, if you compiled it with PyInstaller:

   ```sh
   ./dist/blocker.exe
   ```

2. The application will start minimized to the system tray with a small icon.

3. Right-click the tray icon to access the menu options:
   - **Lock Keyboard**: Manually lock the keyboard.
   - **Unlock Keyboard**: Unlock the keyboard.
   - **Exit**: Close the application.

4. If the keyboard is locked due to inactivity or manually, any key press will display a system message indicating that the keyboard is locked.

## Example Use Cases 🐾

- **Pet Prevention**: Prevent pets like cats from accidentally pressing keys when they walk on your keyboard.
- **Idle Lock**: Automatically lock the keyboard when you step away from your computer to avoid accidental key presses.
- **Focus Mode**: Manually lock the keyboard during focused work or presentations to prevent accidental disruptions.

## Contributing 🤝

If you have suggestions for improvements or find any issues, please open an issue or submit a pull request.

## License 📄

This project is licensed under the MIT License.

---
