#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32


class ResourceListener(Node):
    def __init__(self):
        super().__init__("resource_listener")
        
        self.get_logger().info("Resource listener started")

        self.cpu_sub = self.create_subscription(
            Float32,
            "/cpu_usage",
            self.cpu_callback,
            10
        )

        self.mem_sub = self.create_subscription(
            Float32,
            "/memory_usage",
            self.mem_callback,
            10
        )

        self.get_logger().info("Resource Listener Node started")

    def cpu_callback(self, msg):
        self.get_logger().info(f"CPU: {msg.data:.1f} %")

    def mem_callback(self, msg):
        self.get_logger().info(f"Memory: {msg.data:.1f} %")


def main():
    rclpy.init()
    node = ResourceListener()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
