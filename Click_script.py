#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Click_script.py
#  
#  Copyright 2017 raja <raja@raja-Inspiron-N5110>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
import sys
import os
import pygame
import pygame.camera as wiecam
from pygame.locals import *
import time

pygame.init()
pygame.camera.init()

cam = wiecam.Camera("/dev/video0",(1280,720))
cam.start()
time.sleep(2)
image = cam.get_image()
pygame.image.save(image, "image.jpg")
