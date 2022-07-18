import olympe
import os

from olympe.messages.ardrone3.Piloting import TakeOff, moveBy, Landing
from olympe.messages.ardrone3.PilotingState import FlyingStateChanged

DRONE_IP = os.environ.get("DRONE_IP", "192.168.42.1")

def test_takeoff_docker():
    drone = olympe.Drone(DRONE_IP)
    drone.connect()
    
    assert drone(TakeOff()).wait().success()
    assert drone(
        moveBy(10, 0, 0, 0) 
        >> FlyingStateChanged(state="hovering", _timeout=5)
    ).wait().success()    
    assert drone(Landing()).wait().success()

    drone.disconnect()

if __name__ == "__main__":
    test_takeoff_docker()