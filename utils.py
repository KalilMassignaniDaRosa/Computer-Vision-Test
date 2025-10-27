import base64
from io import BytesIO
from config import DEBUG


def debug_print(message: str):
    """Mostra mensagem debug se DEBUG estiver ativado"""
    if DEBUG:
        print(f"[DEBUG] {message}")


def image_to_base64(img, quality: int = 85) -> str:
    """Converte imagem PIL para Base64 (JPEG)"""
    with BytesIO() as buffer:
        img.save(buffer, format="JPEG", quality=quality)
        encoded = base64.b64encode(buffer.getvalue()).decode("utf-8")

    debug_print(f"Image converted to Base64 ({len(encoded)} characters)")
    return encoded


def print_menu(options: list[str]):
    """Mostra o menu principal"""
    print("\n+------------+")
    print("| Gemini APP |")
    print("+------------+\n")

    for i, option in enumerate(options, 1):
        print(f"[{i}] {option}")

    print_separator()


def print_controls(controls: dict[str, str]):
    """Mostra os controles disponíveis dentro de uma caixa formatada"""
    # Calcula a largura necessária baseada no maior texto
    max_width = max(len(f"{key} → {desc}") for key, desc in controls.items())
    box_width = max(max_width + 4, 20)  # Mínimo de 20, +4 para padding
    
    # Cabeçalho da caixa
    print("\n+" + "-" * (box_width - 2) + "+")
    print("|" + "CONTROLS".center(box_width - 2) + "|")
    print("+" + "-" * (box_width - 2) + "+")
    
    # Exibe cada controle dentro da caixa
    for key, description in controls.items():
        line = f"{key} → {description}"
        print("|" + f" {line:<{box_width - 3}}" + "|")
    
    # Rodapé da caixa
    print("+" + "-" * (box_width - 2) + "+\n")


def print_analysis_with_bars(analysis: str):
    """Mostra o texto de análise dentro de uma caixa formatada com quebra de linha"""
    if not analysis.strip():
        print("[INFO] No analysis available\n")
        return

    max_line_width = 70  # Largura máxima para não ultrapassar o terminal
    
    # Quebra o texto em linhas respeitando a largura máxima
    words = analysis.split()
    lines = []
    current_line = ""
    
    for word in words:
        # Testa se a palavra cabe na linha atual
        if len(current_line) + len(word) + 1 <= max_line_width:
            current_line += (word + " ")
        else:
            # Salva a linha atual e começa uma nova
            if current_line:
                lines.append(current_line.rstrip())
            current_line = word + " "
    
    # Adiciona a última linha
    if current_line:
        lines.append(current_line.rstrip())
    
    # Calcula a largura da caixa baseada na maior linha
    box_width = min(max(len(line) for line in lines) + 4, max_line_width + 4)
    
    # Cabeçalho da caixa
    print("\n+" + "=" * (box_width - 2) + "+")
    print("|" + "ANALYSIS".center(box_width - 2) + "|")
    print("+" + "=" * (box_width - 2) + "+")
    
    # Imprime cada linha dentro da caixa
    for line in lines:
        print("|" + f" {line:<{box_width - 3}}" + "|")
    
    # Rodapé da caixa
    print("+" + "=" * (box_width - 2) + "+\n")


def print_status(message: str, status_type: str = "info"):
    """Mostra mensagem de status com label apropriada"""
    labels = {
        "info": "INFO",
        "success": "SUCCESS",
        "error": "ERROR",
        "waiting": "WAITING",
        "process": "PROCESS"
    }
    label = labels.get(status_type.lower(), "INFO")
    print(f"[{label}] {message}")


def print_separator(line_break: bool = True):
    """Imprime linha separadora"""
    print(("\n" if line_break else "") + "=" * 30)