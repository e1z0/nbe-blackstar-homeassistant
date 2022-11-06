# NBE Blackstar+/RTB Pellet Burners Home Assistant Integration

<img src="https://github.com/e1z0/nbe-blackstar-homeassistant/raw/master/pics/nbe_blackstar_plus.png" width=45% height=45%><img src="https://github.com/e1z0/nbe-blackstar-homeassistant/raw/master/pics/nbe1.png" width=45% height=45%>

**Runs as service or as docker container**

# Requirements

* MQTT Broker server
* Home Assistant or compatible home automation system OpenHab, IoBroker, Node-Red etc...

# Compatible Pellet Burners

* NBE RTB 10 (v13 controller)
* NBE RTB 10 VAC (v13 controller)
* NBE RTB 16 (v13 controller)
* NBE RTB 16 VAC (v13 controller)
* NBE RTB 30 (v13 controller)
* NBE RTB 30 VAC (v13 controller)
* NBE RTB 50 (v13 controller)
* NBE RTB 50 VAC (v13 controller)
* NBE RTB 80 (v13 controller)
* NBE BS+ (Blackstar+) 10 (v13 controller)
* NBE BS+ (Blackstar+) 16 (v13 controller)
* NBE BS+ (Blackstar+) 25 (v13 controller)

If you don't know what model you are using, try to open pellet burner door and look over there, then compare with the user manual of most common models, it can be found [here](https://www.nbe.dk/wp-content/uploads/2017/07/RTB-BS-Manual-V13-ENG-08.03.2017.pdf)

# How to run?

```
make up
```
It will bring docker up, docker system must be already running on the host system. You can edit compose file for different options and set nbe serial and password.

* **NBE Serial** can be found on system menu System > User account > Serial number on the controller
* **NBE Password** can be found on the pallet burner phisically just open the door and look at the top, it should be written over there.

# Standard install (without docker)

Move files from **src/** to **/opt/nbe** and do not forget to copy **nbe.service** to **/etc/systemd/system**, edit **config.json**, enable and start the service
```
pip3 install pycrypto paho-mqtt simplejson
systemctl enable nbe&&systemctl start nbe
```

# Features

What features are working by now:
* Various sensors
* Climate control for hot water
* Climate control for pellet burner itself

# TODO

* Different zones regulation as climate control or similar
* Turn on/off pellet burner
* <del>Climate control</del>
* Cross platform docker images


# Customization

<img src="https://github.com/e1z0/nbe-blackstar-homeassistant/raw/master/pics/nbe2.png" width=40% height=40%>

You can enable different sensors, controls, etc..  just look at **nbe_schema** file..

The main configuration lies in config.json, just modify to suit your needs.
