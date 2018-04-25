# RPI Jukebox

Basic Raspberry Pi Radio Jukebox

## TODO:

* Dockerise everything
* Improve README.md

## Requirements

* Python 3.6.5 or greater
* Systemd Linux Distro
* VLC Media Player

## Installation

Clone this repo into `/opt`:
```shell
git clone https://github.com/cpressland/rpi-jukebox.git /opt/rpi-jukebox
```

Move the included Systemd unit into `/etc/systemd/system`
```shell
mv /opt/rpi-jukebox/systemd_units/jukebox.service /etc/systemd/system/jukebox.service
```

## Usage

Simply call `/` via `curl localhost:5000` for documentation
