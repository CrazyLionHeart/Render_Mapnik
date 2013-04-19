#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Source: http://wiki.openstreetmap.org/wiki/Slippy_map_tilenames

import math
import sys

def deg2num(lat_deg, lon_deg, zoom):
  lat_rad = math.radians(lat_deg)
  n = 2.0 ** zoom
  xtile = int((lon_deg + 180.0) / 360.0 * n)
  ytile = int((1.0 - math.log(math.tan(lat_rad) + (1 / math.cos(lat_rad))) / math.pi) / 2.0 * n)
  return (xtile, ytile)

lat = float(sys.argv[1])
lon = float(sys.argv[2])
zoom = sys.argv[3]

x,y = deg2num(lat, lon, float(zoom))
print "%s %s %s" % (x, y, zoom)

