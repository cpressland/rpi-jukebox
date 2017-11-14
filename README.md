# RPI Jukebox

Basic Raspberry Pi Radio Jukebox

## TODO:

* Improve all the things.

## Installation

Requires any systemd based Linux Distribution.

### Copy files

```
cp systemd_units/* /etc/systemd/system/
cp tuner.rb /opt/tuner.rb
```

### Install Ruby

`apt-get install ruby`
`gem install sinatra`

## Usage

### Control Mode

Control Mode has the following options:

* start
* stop
* restart

### Station Mode

Station Mode has the following options:

* classicrock
* absoluteradio

### Examples

Start the Jukebox
`curl http://<ipaddress>:4567/control/start`

Change the Station
`curl http://<ipaddress>:4567/station/classicrock`
