import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Listener(Node):
    def __init__(self):
        super().__init__('listener')

        self.subscription = self.create_subscription(
            String,
            'TESTchatter',
            self.callback,
            10
        )

    def callback(self, msg):
        self.get_logger().info('受信: "%s"' % msg.data)

def main():
    rclpy.init()
    node = Listener()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
