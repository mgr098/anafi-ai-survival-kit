# GroundSDK Flightplan Guide 📝

This document contains instructions on how to manage GroundSDK flightplans for the ANAFI Ai drone.

## Prerequisites ✔

* A WiFi connection to the ANAFI Ai drone

## Creating Flightplan 🗺️

Flightplans can be created by 
* [Parrot Mavlink docs](https://developer.parrot.com/docs/mavlink-flightplan/overview.html)
* [QGroundControl](https://docs.qgroundcontrol.com/master/en/getting_started/download_and_install.html)

Use the QGC to MAVlink converter to convert your QGC plans to .mavlink files by running
```
python3 convert.py /plans/qgc.plan
```

<details>
<summary> Example flightplan provided by Parrot </summary>
<br>

```
QGC WPL 120
0   1       3       22      15.000000       0.000000        0.000000        nan     48.878601       2.366549        15.000000       1
1   0       3       16      0.000000        0.000000        0.000000        0.000000        48.879000       2.366549        20.000000       1
2   0       2       2000    0.000000        1.000000        1.000000        1.000000        0.000000        0.000000        0.000000        1
3   0       2       93      10.000000       0.000000        0.000000        0.000000        0.000000        0.000000        0.000000        1
4   0       2       2001    0.000000        0.000000        0.000000        0.000000        0.000000        0.000000        0.000000        1
5   0       3       21      0.000000        0.000000        0.000000        nan     48.879139       2.367296        0.000000        1
```

This flightplan will tell the drone to takeoff, go to waypoint, take a picture, start capture, delay next mav command by 10 seconds, stop capture, and land at current position. Note that the coordinates are from the [Parrot HQ in Paris, France](https://www.google.com/maps/place/48%C2%B052'43.0%22N+2%C2%B021'59.6%22E/@48.878601,2.366549,17z/data=!3m1!4b1!4m5!3m4!1s0x0:0xe818b0ed41a88907!8m2!3d48.878601!4d2.366549), therefore it is not recommended to run this flightplan on your drone.

</details>


## View Flightplans 🧐

GroundSDK flightplans can be viewed from these addresses   
* http://anafi-ai.local (Real and simulated, whichever is connected)
* http://192.168.42.1 (Real only)

There are three ways to view flightplans

1. Navigate to Flightplan tab on drone webserver http://192.168.42.1
2. Running ```curl -X GET "http://anafi-ai.local/api/v1/upload/flightplans"``` in your terminal

In order to view flightplan content, run 
```
curl "http://anafi-ai.local/api/v1/upload/{flightplan_uid}" 
```
Remember to replace id with id flightplan id

## Upload Flightplan ⬆️

There are three ways to upload a GroundSDK flightplan

1. Go to Flightplan tab on drone webserver http://192.168.42.1/#/ , click upload button and choose a mavlink file
2. Running  ```curl -i -X PUT "http://anafi-ai.local/api/v1/upload/flightplan" --data-binary @"<flightplan>"``` (Note: replace ```flightplan```)
3. Run Parrot Olympe Python script ```python3 upload.py /plans/flightplan``` (Note: This will also activate flightplan)

<details>
<summary> The python script requires Parrot Olympe, but can be used with Docker if this is not installed.</summary>
To use the Dockerfile, you must first change its file content:
<br>

1. Open Dockerfile and change 
```
11. COPY ./olympe-scripts/gimbal.py .
12. ENTRYPOINT [ "python3", "gimbal.py" ]
```

to 

```
11. COPY upload.py .
12. ENTRYPOINT [ "python3", "upload.py", "./plans/flightplan"]
```
Remember to save the file and set the flightplan location "./plans/flightplan" to your own filepath.

2. Now build image from your terminal ``` docker build -t olympe:latest .```
3. Run the olympe dockerfile from your terminal``` docker run --network host olympe:latest```
</details>


## Activate Flightplan 🚀

There are two? ways of activating a GroundSDK flightplan

1. Run ``` curl -i -X PUT http://anafi-ai.local/api/v1/upload/flightplan/?is_default=yes --data-binary @"<flightplan>```, this will set it to the default flightplan and will start on drone start (Note: Pretty sure this does not work, see [forum post](https://forum.developer.parrot.com/t/too-many-ping-failures-when-connecting-using-docker/16655/4))
2. Run Parrot Olympe Python script ```python3 upload.py /plans/flightplan``` (Note: This will also activate flightplan)

## Downloading Flightplan ⬇️

There are two ways of downloading a GroundSDK Flightplan from the drone

1. Navigate to Flightplan tab on drone webserver http://192.168.42.1 , and press download
2. Run ```curl -X GET http://anafi-ai.local/api/v1/upload/flightplan/{flightplan_uid} ``` in your terminal

## Deleting Flightplan ❌

There are two? ways of deleting a GroundSDK flithplan

1. Restart the drone. Every flightplan is deleted everytime its reset
2. Running ```curl -X DELETE "http://anafi-ai.local/api/v1/upload/flightplans/<id>"``` in your terminal (Note: This doesn't work)
