# OSCWalker

Extremely simple program that allows to track inputs from a Wii Balance Board into steps in VRChat using OSC.

## Windows Defender Screen

The application has to detect inputs at all times and while the windows in unfocused in order to ensure movement reliability.<br>
Because of this, Windows Defender gets a bit scared, as there is an application that is "technically recording all inputs".<br>
While this is "technically true", none of these inputs gets saved anywhere. Have a look at the code. It's only checking if certain buttons are pressed.

## Requirements

### Currently only works/tested with Windows. Have not tested with Linux, and I am not 100% certain that WiiBalanceWalker works on Linux.

- VRChat (It was kind of made for... specifically VRChat)<br>
- Bluetooth<br>
- Uses Pynput (pip install pynput)<br>
- Uses python-osc (pip install python-osc)
- [Uses Python](https://www.python.org/)<br>
- [Uses WiiBalanceWalker by Shachar Liberman](https://github.com/lshachar/WiiBalanceWalker)<br>

## Setup with WiiBalanceWalker

- Run the .EXE file.
- Press the sync/bluetooth button on Wii Balance Board.
- Connect Wii Balance Board to your PC via Bluetooth (Should be labeled starting with "Nintendo").
- When asking for a PIN, press "Add/Remove bluetooth Wii device" button to get your unique PIN code.
- After inputting PIN code, press "Connect to Wii Balance Board" button.
- Confirm connection by stepping on and off, and seeing if values change.
- After connection, set ALL actions under the "Actions" tab to "Do Nothing"
- Set action "Left" to "Key F13" and "Right" to "Key F14".
- Uncheck "Disable All Actions" checkbox.

## Usage

### Windows

If there is a release, download and use that, otherwise:

- Download the zip file by pressing the big green "Code" button, then "Download ZIP".
- Extract the folder and open it.
- While inside the folder, right click empty space and click "Open in Terminal"
- Type and run "python OSCWalker.py"

## Troubleshoot

- Ensure OSC is enabled in the VRChat quick menu.