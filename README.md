# RPI Jukebox

Basic Raspberry Pi Radio Jukebox

## TODO:

* Improve all the things.

## Installation

Requires any systemd based Linux Distribution.

### Copy files

```
cp systemd_units/* /etc/systemd/system/
cp config/hooks.json /etc/hooks.json
cp tuner.rb /opt/tuner.rb
```

### Install Webhook

```
curl -L 'https://github.com/adnanh/webhook/releases/download/2.6.6/webhook-linux-arm.tar.gz' -o '/tmp/webhook.tar.gz'
tar xzvf '/tmp/webhook.tar.gz' -C '/opt' --strip 1
```

### Install Ruby

`apt-get install ruby`

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
`http://<ipaddress>:9000/hooks/jukebox?mode=control&value=start`

Change the Station
`http://<ipaddress>:9000/hooks/jukebox?mode=station&value=classicrock`
