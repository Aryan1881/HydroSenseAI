from hybrid_detector import HybridDrowningDetector

if __name__ == "__main__":
    detector = HybridDrowningDetector(video_source="swimming_video.mp4")  # or 0 for webcam
    detector.run()