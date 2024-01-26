# TODO qui devo importare la rete neurale e passargli l'input, cioe' le letture dei sensori e mi restituira' l'output

#from ANN_controller import ANN_controller
#import numpy as np
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan

class Controller_Node(Node):

    def __init__(self):

        super().__init__('ann_controller')
        self.subscription = self.create_subscription(
            LaserScan,
            'scan',
            self.scan_callback
        )

        self.subscription

    def scan_callback(self, msg):
        self.get_logger().info('ciao')


def main(args=None):

    rclpy.init(args=args)

    controller = Controller_Node
    rclpy.spin(ann_controller)


    

    

if __name__ == '__main__':
    main()
