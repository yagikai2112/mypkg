#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2025 Kaito Yagiuchi
# SPDX-License-Identifier: BSD-3-Clause


from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():

    return LaunchDescription([
        Node(
            package="mypkg",
            executable="cpu_monitor",
            name="cpu_monitor",
            output="screen",
        ),
        Node(
            package="mypkg",
            executable="resource_listener",
            name="resource_listener",
            output="screen",
        ),
    ])
