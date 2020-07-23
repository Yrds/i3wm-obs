# i3wm-obs

This repository contains a simple script that control the source, hiding or showing it depending on selected i3wm workspace.


## Requirements

Install [obs-websocket](https://github.com/Palakis/obs-websocket) plugin and enable the websocket server on "Tools > WebSockets Server Settings"
For python, install the libs: `pip install simpleobsws i3ipc`

## Edit the config

Edit the config.py file to adjust the obs connection and the allowed workspaces that can be seen on obs.

## Running


Open OBS and run `python3 ./main.py`
