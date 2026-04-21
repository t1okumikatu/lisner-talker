import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Talker(Node):
    def __init__(self):
        super().__init__('talker')

        self.publisher_ = self.create_publisher(String, 'TESTchatter', 10)
        self.timer = self.create_timer(1.0, self.timer_callback)
        self.count = 0

    def timer_callback(self):
        msg = String()
        msg.data = f'Hello {self.count}'
        self.publisher_.publish(msg)
        self.get_logger().info(f'送信: "{msg.data}"')
        self.count += 1

def main():
    rclpy.init()
    node = Talker()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
