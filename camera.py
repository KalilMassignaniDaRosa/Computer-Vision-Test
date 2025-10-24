import cv2
from config import CAMERA_INDEX, FRAME_WIDTH, FRAME_HEIGHT
from utils import debug_print, print_status
from PIL import Image

class CameraManager:
    def __init__(self, camera_index=CAMERA_INDEX):
        self.camera_index = camera_index
        self.cap = None

    def initialize(self):
        """Inicializa camera"""
        print_status("Initializing camera...", "process")
        debug_print(f"Camera index: {self.camera_index}")
        
        self.cap = cv2.VideoCapture(self.camera_index)
        
        if not self.cap.isOpened():
            print_status(f"Could not open camera {self.camera_index}", "error")
            raise SystemExit(f"Error: Could not open camera {self.camera_index}")
        
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, FRAME_WIDTH)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, FRAME_HEIGHT)

        print_status(f"Camera initialized: {FRAME_WIDTH}x{FRAME_HEIGHT}", "success")
        debug_print(f"Camera initialized: {FRAME_WIDTH}x{FRAME_HEIGHT}")

    def capture_frame(self):
        """Captura frame"""
        ret, frame = self.cap.read()

        if not ret:
            debug_print("Failed to capture frame!")
            return None
        
        debug_print(f"Frame captured: {frame.shape}")
        return frame

    def release(self):
        """Libera recursos"""
        if self.cap:
            self.cap.release()
            cv2.destroyAllWindows()
            print_status("Camera released", "success")
            debug_print("Camera released!")

    @staticmethod
    def frame_to_pil(frame):
        """Converte OpenCV BGR para PIL RGB"""
        from cv2 import cvtColor, COLOR_BGR2RGB
        return Image.fromarray(cvtColor(frame, COLOR_BGR2RGB))
