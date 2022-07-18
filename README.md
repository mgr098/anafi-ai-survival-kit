# ANAFI AI Survival Kit ✈️

Survival kit for the ANAFI Ai Parrot Drone, contains scripts and guides to manage GroundSDK Flightplans.

## Download

```
git clone anafi-ai-survival-kit
```

## Creating Fligthplan

### Using QGC

### Freehand

## Upload & Activate Flightplan

ip address can either be: anafi-ai.local, 192.168.42.1.
This guide will use 192.168.42.1 since it only refers to the real drone. The other ip will route to whichever anafi ai that is connected to the wifi whether its real or simulated.

There are three ways to view flightplans

1. go to website
2. curl -X GET "http://anafi-ai.local/api/v1/upload/flightplans"
3. parrot olympe

View content
 curl "http://anafi-ai.local/api/v1/upload/<id>" --> remember to replace id with id flightplan id

There are three ways to upload a flightplan

1. go to http://192.168.42.1/#/ flightplans and click upload
2. use curl -i -X PUT "http://anafi-ai.local/api/v1/upload/flightplan" --data-binary @"1-takeoff-land"
3. use parrot olympe

However, there are two ways of activating (starting) the flightplan

1. use curl PUT /api/v1/mission/missions/?is_default=yes
2. use parrot olympe

Remember to reference the binary correctly.

Note: Missions can't be uploaded twice. 

There are two ways to delete flightplans

1. turn drone off
2.

