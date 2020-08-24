#!/usr/bin/env python3
"""
This policy should place the end effector of the 3 fingers on the object.
"""
import numpy as np
import rrc_simulation
from scipy.spatial.transform import Rotation
import time

_CUBE_WIDTH = 0.065

platform = rrc_simulation.TriFingerPlatform(visualization=True)

# Current pose of the object
object_pose = rrc_simulation.trifinger_platform.ObjectPose()

position = object_pose.position
orientation = object_pose.orientation