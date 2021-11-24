automate-home lights example project
====================================

An example project for the [automate-home project](https://github.com/majamassarini/automate-home).

A collection of files which define automation rules for 4 different lights **Appliances**.

- [light.presence.Appliance](https://automate-home.readthedocs.io/en/latest/appliances.html#light-presence-appliance)
- [light.zone.Appliance](https://automate-home.readthedocs.io/en/latest/appliances.html#light-zone-appliance)
- [light.indoor.dimmerable.Appliance](https://automate-home.readthedocs.io/en/latest/appliances.html#light-indoor-dimmerable-appliance)
- [light.indoor.hue.Appliance](https://automate-home.readthedocs.io/en/latest/appliances.html#light-indoor-hue-appliance)

Every *Appliance* automates a device, through a *Performer*.
The automated devices are 2 **KNX** switches, 1 **KNX** dimmer and 1 **Lifx** bulb (switched on/off by one more **KNX** switch).

To automate the lights two sensors, other than the buttons, are used:

- [sensor.luxmeter.Appliance](https://automate-home.readthedocs.io/en/latest/appliances.html#sensor-luxmeter-appliance); data come from a **KNX** sensor.
- [sensor.alarm.Appliance](https://automate-home.readthedocs.io/en/latest/appliances.html#sensor-alarm-appliance); data come from **KNX**.

## Project notes
  1. The buttons, in this project, have not an associated Appliance model, their *KNX* messages are directly delivered to the lights Appliances through the *Performers*.  
  2. The *Lifx* bulb is controlled using scheduler triggers with some seconds delay; 
     it is turned on/off through a *KNX* switch and it takes 7/8 seconds to be ready to listen and execute *Lifx* commands.
     This is an example of a **single Appliance with two controlled devices**.

## Run automate-home docker container using this project files

```shell
export AUTOMATE_HOME_CONFIGURATION=`pwd`
export NETWORK_NAME='qnet-static-eth0-a7611e'
export IP='172.31.10.243'

docker run -dit --privileged --name lights --network $NETWORK_NAME --ip $IP -p 8181:8181 -v graphite-lights:/opt/graphite/storage -v redis-lights:/var/lib/redis -v "$AUTOMATE_HOME_CONFIGURATION:/etc/automate-home" -t majamassarini/automate-home:latest
docker exec -it lights /bin/bash
```

## UI

[GUI example](https://majamassarini.github.io/automate-lights-example/pages/172.31.10.243/index.html)
