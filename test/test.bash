#!/bin/bash

dir=~
[ "$1" != "" ] && dir="$1"

cd "$dir/ros2_ws" || exit 1
colcon build > /dev/null 2>&1 || exit 1

source /opt/ros/humble/setup.bash > /dev/null 2>&1
source install/setup.bash > /dev/null 2>&1

timeout 10 ros2 launch mypkg cpu_monitor.launch.py \
  > /tmp/mypkg.log 2>&1

grep -q "/cpu_usage" /tmp/mypkg.log || exit 1
grep -q "/memory_usage" /tmp/mypkg.log || exit 1

grep -q "Received CPU=" /tmp/mypkg.log || exit 1

exit 0

