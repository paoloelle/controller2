# TODO qui devo importare la rete neurale e passargli l'input, cioe' le letture dei sensori e mi restituira' l'output

#from ANN_controller import ANN_controller
#import numpy as np
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from rclpy.qos import qos_profile_sensor_data

class Controller_Node(Node):

    def __init__(self):

        super().__init__('ann_controller')
        self.subscription = self.create_subscription(
            LaserScan,
            'scan',
            self.scan_callback,
            10
        )

        self.subscription

        self.publisher = self.create_publisher(LaserScan, 'filtered_scan', 10)

        self.min_angle = -2.5
        self.max_angle = -0.5



    

    def scan_callback(self, msg):
        
        min_index = int((self.min_angle - msg.angle_min) / msg.angle_increment)
        max_index = int((self.max_angle - msg.angle_min) / msg.angle_increment)

        min_index = max(0, min(min_index, len(msg.ranges) - 1))
        max_index = max(0, min(max_index, len(msg.ranges) - 1))


        filtered_ranges = msg.ranges[min_index:max_index-1]

        filtered_scan = LaserScan()
        filtered_scan.header = msg.header
        filtered_scan.angle_min = self.min_angle
        filtered_scan.angle_max = self.max_angle
        filtered_scan.angle_increment = msg.angle_increment
        filtered_scan.scan_time = msg.scan_time
        filtered_scan.range_min = msg.range_min
        filtered_scan.range_max = msg.range_max
        filtered_scan.ranges = filtered_ranges
        filtered_scan.intensities = msg.intensities

        print(len(filtered_ranges))

        self.publisher.publish(filtered_scan)


def main(args=None):

    rclpy.init(args=args)

    ann_controller = Controller_Node()
    rclpy.spin(ann_controller)
    
    ann_controller.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
