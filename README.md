# OSCWalker

Extremely simple program that allows to track inputs from a Wii Balance Board into steps in VRChat using OSC.

## Requirements

- VRChat (It was kind of made for... specifically VRChat)<br>
- Bluetooth<br>
- Uses Pygame (pip install pygame)<br>
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

- After setting up, simply run the Python application.

## Troubleshoot
- Ensure that pygame is installed.
- Ensure that the pygame window is focused.
- Ensure OSC is enabled in the VRChat quick menu.