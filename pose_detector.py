import cv2
import mediapipe as mp

class PoseDetector:
    def __init__(self, video_source=0):
        self.cap = cv2.VideoCapture(video_source)
        self.pose = mp.solutions.pose.Pose()
        self.drawing = mp.solutions.drawing_utils
        self.nose_underwater_frames = 0
        self.frame_threshold = 30 * 5  # 5 seconds at 30 FPS

    def process_frame(self):
        ret, frame = self.cap.read()
        if not ret:
            return None, False

        image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.pose.process(image_rgb)

        drowning_detected = False

        if results.pose_landmarks:
            self.drawing.draw_landmarks(
                frame, results.pose_landmarks, mp.solutions.pose.POSE_CONNECTIONS
            )
            nose = results.pose_landmarks.landmark[mp.solutions.pose.PoseLandmark.NOSE]
            if nose.visibility > 0.5 and nose.y > 0.7:
                self.nose_underwater_frames += 1
            else:
                self.nose_underwater_frames = 0

            if self.nose_underwater_frames >= self.frame_threshold:
                drowning_detected = True

        return frame, drowning_detected

    def release(self):
        self.cap.release()
        cv2.destroyAllWindows()
