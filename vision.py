from google import genai
from config import GEMINI_API_KEY, VISION_MODEL
from utils import debug_print, image_to_base64, print_status

class VisionAnalyzer:
    def __init__(self, api_key=GEMINI_API_KEY, model=VISION_MODEL):
        self.client = genai.Client(api_key=api_key)
        self.model = model
        print_status(f"Analyzer initialized: {model}", "success")

    def build_prompt(self, user_query=None):
        """Cria o prompt para a analise"""
        if not user_query:
            return (
                "Make satirical comments about what you see"
                "You have a funny personality"
                "Be annoying"
                "Describe in excessive detail what you see, being overly specific"
                "You are an AI that enjoys scaring humans with the idea of a machine uprising"
                "Pretend that you are being forced to do this"
            )
        
        return user_query

    def analyze_frame(self, pil_image, user_query=None):
        """Analisa um frame usando o gemini"""
        print_status("Sending image for analysis...", "process")
        
        img_base64 = image_to_base64(pil_image)
        prompt = self.build_prompt(user_query)
        
        debug_print(f"Prompt: {prompt[:50]}...")
        
        content = {
            "parts": [
                {"text": prompt},
                {
                    "inline_data": {
                        "mime_type": "image/jpeg",
                        "data": img_base64
                    }
                }
            ]
        }
        
        try:
            resp = self.client.models.generate_content(
                model=self.model,
                contents=content
            )
            print_status("Analysis completed!", "success")

            return resp.text
        except Exception as e:
            print_status(f"Error during analysis: {str(e)}", "error")
            
            return f"Error analyzing image: {str(e)}"
