#!/usr/bin/env python3
"""
This policy should place the end effector of the 3 fingers on the object.
"""

from scipy.spatial.transform import Rotation
import time
import numpy as np

import rrc_simulation

platform = rrc_simulation.TriFingerPlatform(visualization=True)

# Cube pose at time stamp zero
cube_pose = platform.get_object_pose(0.0)

# Initial position of the cube
cube_position = cube_pose.position

r = Rotation.from_quat(cube_pose.orientation)

# Initial orientation of the cube as euler angles
cube_orientation = r.as_euler('xyz')

sim_finger = rrc_simulation.SimFinger('trifingerpro')

# Initial observation
observation = sim_finger.get_observation(0.0)

# Robot finger pose
finger_zero_postion = observation.position[:3]
finger_one_position = observation.position[3:6]
finger_two_position = observation.position[6:]

_CUBE_WIDTH = 0.065