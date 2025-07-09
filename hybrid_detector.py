from pose_detector import PoseDetector
from sensor_simulator import SensorSimulator
from alert_system import AlertSystem
import cv2

class HybridDrowningDetector:
    def __init__(self, video_source=0):
        self.pose_detector = PoseDetector(video_source)
        self.sensor_simulator = SensorSimulator()
        self.alert_system = AlertSystem()

    def run(self):
        while True:
            frame, pose_alert = self.pose_detector.process_frame()
            if frame is None:
                break

            sensor_alert = self.sensor_simulator.is_pressure_high()

            if pose_alert or sensor_alert:
                self.alert_system.trigger_alert()

            cv2.imshow("Drowning Detection System", frame)
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break

        self.pose_detector.release()