import olympe
import os

from olympe.messages.ardrone3.Piloting import TakeOff, moveBy, Landing
from olympe.messages.ardrone3.PilotingState import FlyingStateChanged
from olympe.messages.ardrone3.GPSSettingsState import GPSFixStateChanged

DRONE_IP = os.environ.get("DRONE_IP", "192.168.42.1")

def test_takeoff_docker():
    drone = olympe.Drone(DRONE_IP)
    drone.connect()
    
    # Automatic takeoff
    drone(
        FlyingStateChanged(state="hovering", _policy="check")
        | FlyingStateChanged(state="flying", _policy="check")
        | (
            GPSFixStateChanged(fixed=1, _timeout=5, _policy="check_wait")
            >> (
                TakeOff(_no_expect=True)
                & FlyingStateChanged(
                    state="hovering", _timeout=5, _policy="check_wait"
                )
            )
        )
    ).wait()

    assert drone(
        moveBy(10, 0, 0, 0) 
        >> FlyingStateChanged(state="hovering", _timeout=5)
    ).wait().success()
        
    assert drone(Landing()).wait().success()

    drone.disconnect()

if __name__ == "__main__":
    test_takeoff_docker()