Automate Home Lights example project
====================================

A collection of files which define automation rules for lights **Appliances**.

Automated **Appliances**:

 - light.presence.Appliance
 - light.zone.Appliance
 - light.indoor.dimmerable.Appliance
 - light.indoor.hue.Appliance

## Run Automate Home docker container using this project files

```shell
export AUTOMATE_HOME_CONFIGURATION=`pwd`
export NETWORK_NAME='qnet-static-eth0-a7611e'
export IP='172.31.10.243'

docker run -dit --privileged --name lights --network $NETWORK_NAME --ip $IP -p 8181:8181 -v graphite-lights:/opt/graphite/storage -v redis-lights:/var/lib/redis -v "$AUTOMATE_HOME_CONFIGURATION:/etc/automate-home" -t automate-home/complete-node:latest
docker exec -it lights /bin/bash
```

## UI

[GUI example](https://majamassarini.github.io/automate-lights-example/pages/172.31.10.243/index.html)

