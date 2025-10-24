import base64
from io import BytesIO
from config import DEBUG

def debug_print(message: str):
    """Mensagem DEBUG"""
    if DEBUG:
        print(f"[DEBUG] {message}")

def image_to_base64(img, quality=85):
    """Converte imagem PIL para base64 JPEG"""
    buffer = BytesIO()
    img.save(buffer, format="JPEG", quality=quality)

    img_bytes = buffer.getvalue()
    img_base64 = base64.b64encode(img_bytes).decode('utf-8')

    debug_print(f"Image converted to base64: {len(img_base64)} characters")

    return img_base64

def print_header(title: str, width=80):
    """Imprime o header"""
    print("\n" + "=" * width)
    title_padded = f" {title} ".center(width, "=")
    print(title_padded)
    print("=" * width + "\n")

def print_menu(options: list):
    """Imprime o menu"""
    print_header("GEMINI VISION APP")

    for i, option in enumerate(options, 1):
        print(f"  [{i}] {option}")
        
    print()

def print_controls(controls: dict):
    """Imprime os controles"""
    print("\n" + "-" * 60)
    print("CONTROLS:")
    print("-" * 60)

    for key, description in controls.items():
        print(f"  {key:8} -> {description}")

    print("-" * 60 + "\n")

def print_analysis_with_bars(analysis: str):
    """Imprime analise com barras"""
    lines = analysis.split('\n')
    max_line_length = max(len(line) for line in lines) if lines else 40
    bar_length = min(max(max_line_length, 40), 80)
    
    print("\n" + "=" * bar_length)
    print(" ANALYSIS ".center(bar_length, "="))
    print("=" * bar_length)
    print(analysis)
    print("=" * bar_length + "\n")

def print_status(message: str, status_type="info"):
    """Imprime status"""
    status_labels = {
        "info": "INFO",
        "success": "SUCCESS",
        "error": "ERROR",
        "waiting": "WAITING",
        "process": "PROCESS"
    }
    label = status_labels.get(status_type, "INFO")
    print(f"[{label}] {message}")

def print_separator(char="-", length=60):
    """Imprime linha separadora"""
    print("\n" + char * length)
