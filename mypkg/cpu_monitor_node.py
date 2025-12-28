import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import psutil


class CpuMonitorNode(Node):
    def __init__(self):
        super().__init__("cpu_monitor")

        self.declare_parameter("publish_rate", 1.0)
        rate = self.get_parameter("publish_rate").value

        self.cpu_pub = self.create_publisher(Float32, "cpu_usage", 10)
        self.mem_pub = self.create_publisher(Float32, "memory_usage", 10)

        self.timer = self.create_timer(1.0 / rate, self.publish_usage)
        self.get_logger().info("CPU Monitor Node started")

    def publish_usage(self):
        cpu_msg = Float32()
        mem_msg = Float32()

        cpu_msg.data = float(psutil.cpu_percent())
        mem_msg.data = float(psutil.virtual_memory().percent)

        self.cpu_pub.publish(cpu_msg)
        self.mem_pub.publish(mem_msg)


def main():
    rclpy.init()
    node = CpuMonitorNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
