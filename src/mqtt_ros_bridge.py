import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import paho.mqtt.client as mqtt
import json

class MqttRosBridge(Node):
    def __init__(self):
        super().__init__('mqtt_ros_bridge')
        self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 10)
        
        # MQTTの設定
        self.mqtt_client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2)
        self.mqtt_client.on_message = self.on_message
        self.mqtt_client.connect("localhost", 1883, 60)
        self.mqtt_client.subscribe("robot/joystick")
        self.mqtt_client.loop_start()
        self.get_logger().info('MQTT-ROS Bridge Node has started')

    def on_message(self, client, userdata, msg):
        try:
            data = json.loads(msg.payload)
            twist = Twist()
            # スティックの値を速度指令にマッピング
            # スティックの上方向が y: -1.0 なので反転させています
            twist.linear.x = -float(data['y']) 
            twist.angular.z = -float(data['x'])
            
            self.publisher_.publish(twist)
        except Exception as e:
            self.get_logger().error(f'Error parsing message: {e}')

def main():
    rclpy.init()
    node = MqttRosBridge()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
