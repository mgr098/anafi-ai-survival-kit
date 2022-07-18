# ANAFI AI Survival Kit ✈️

Survival kit for the [ANAFI Ai Parrot Drone](https://www.parrot.com/en/drones/anafi-ai), contains scripts to manage [GroundSDK Flightplans](https://developer.parrot.com/docs/mavlink-flightplan/overview.html).

## Repository Structure 🗃️
```
├── src
|   ├── /flightplans                Folder containing GroundSDK Flightplans
|   ├── /olympe-scripts             Folder containing Parrot Olympe python scripts
|   |   └── gimbal.py               Moves the ANAFI Ai gimbal    
|   |   └── move.py                 Takeoff, move and land ANAFI Ai    
|   ├── convert.py                  Converts QGC JSON .plan to .mavlink
|   ├── Dockerfile                  Parrot Olympe Dockerfile
|   ├── README.md                   Contains instructions on how to manage GroundSDK missions
|   └── upload.py                   Uploads GroundSDK mission to ANAFI Ai and activates it    
└── README.md                       This README
```
## Prerequisites ✔

* [Anafi AI Drone](https://www.parrot.com/en/drones/anafi-ai)
* [Python3](https://www.python.org/downloads)
* [Docker](https://docs.docker.com/get-docker/)  
* [QGroundControl (QGC)]() 
* [Parrot Olympe](https://developer.parrot.com/docs/olympe/installation.html) (Recommended, but not required)

## Setup ⚙️

Clone the project and navigate to the /src folder
```
git clone https://github.com/mgr098/anafi-ai-survival-kit.git
cd src
```

## Usage 🖥

### Converter ♻️

To convert QGC plan to mavlink file, run this in your terminal
```
python3 convert.py /plans/qgc.plan
```

<details>
<summary> Optional Arguments </summary>
<br>

```
python3 convert.py --help
```
Output
```
usage: convert.py [-h] [--out OUT] [--version VERSION]
               [--takeoff TAKEOFF]
               filepath

Convert QGC .plan to .mavlink format

positional arguments:
  filepath           Usage: python3 convert.py </path/to/file/>

optional arguments:
  -h, --help         show this help message and exit
  --out OUT          MAVlink filename
  --version VERSION  MAVlink version
  --takeoff TAKEOFF  Add takeoff at start of mavlink
```
Example usecase of optional arguments

```
python3 convert.py qgc.plan --out output.mavlink --version 120 --takeoff True
```
</details>


### Upload ⬆️

To upload a .mavlink file to the drone and activate the GroundSDK flightplan, run this in your terminal
```
python3 upload.py /plans/flightplan.mavlink
```

### Olympe Dockerfile 🐋

The Dockerfile creates a Docker image running Parrot Olympe. Run this in your terminal to build it
```
docker build -t olympe:latest .
```

Run the olympe dockerfile 

```
docker run --network host olympe:latest
```



