#!/bin/bash

for z in {1..18}
do
        echo "Generate tile for lat: $x, lon: $y, zoom: $z"
        tile_min=$(python generate_tile.py 54 36 $z)
        tile_max=$(python generate_tile.py 56 38 $z)
        min_x=$tile_min[0]
        max_x=$tile_max[0]
        min_y=$tile_min[1]
        max_y=$tile_max[1]
        render_list --all --socket=/var/run/renderd/renderd.sock --num-threads=2 -x $min_x -X $max_x -y $min_y -Y $max_y  --min-zoom=$z --max-zoom=$z
done

