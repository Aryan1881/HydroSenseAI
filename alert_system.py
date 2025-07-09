from playsound import playsound

class AlertSystem:
    def __init__(self, sound_file="alert_sound.mp3"):
        self.sound_file = sound_file

    def trigger_alert(self):
        print("🚨 ALERT: Possible Drowning Detected!")
        try:
            playsound(self.sound_file)
        except:
            print("⚠️ Unable to play sound. Please check alert_sound.mp3.")
