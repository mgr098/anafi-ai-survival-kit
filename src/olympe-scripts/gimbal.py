import os
from telnetlib import IP
import time
import argparse

import olympe
from olympe.messages import gimbal

TIMEOUT = 120
REAL_IP = "192.168.42.1"

DRONE_IP = os.environ.get("DRONE_IP", REAL_IP)
DRONE_MEDIA_PORT = os.environ.get("DRONE_MEDIA_PORT", "80")

# Set logging level to info
olympe.log.update_config({"loggers": {"olympe": {"level": "INFO"}}})

def parse_args():
    parser = argparse.ArgumentParser(
        description="Connect to the drone and move its gimbal")

    parser.add_argument(
        "ip", type=str, help="Usage: python3 real.py <drone ip>", default=REAL_IP)

    return parser.parse_args()

def main(drone_ip):
    drone = olympe.Drone(drone_ip, media_port=DRONE_MEDIA_PORT)
    drone.connect(retry=3)

    pitches = [-90, 0, 90, -90, 0, -90, 0]
    
    for _pitch in pitches:
        drone(gimbal.set_target(
            gimbal_id=0,
            control_mode="position",
            yaw_frame_of_reference="none",   # None instead of absolute
            yaw=0.0,
            pitch_frame_of_reference="absolute",
            pitch=_pitch,
            roll_frame_of_reference="none",     # None instead of absolute
            roll=0.0,
        )).wait().success()

        time.sleep(3)
        
    drone.disconnect()

if __name__ == "__main__":
    # args = parse_args()
    main(REAL_IP)