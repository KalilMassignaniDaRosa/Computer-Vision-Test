import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise SystemExit("Error: GEMINI_API_KEY not found in .env")

DEBUG = False

VISION_MODEL = "gemini-2.0-flash-exp"  # Modelo com suporte a visao
CAMERA_INDEX = 0  # Indice da camera (0 = camera padrao)
FRAME_WIDTH = 640  # Largura do frame
FRAME_HEIGHT = 480  # Altura do frame
JPEG_QUALITY = 85  # Qualidade da imagem JPEG (1-100)