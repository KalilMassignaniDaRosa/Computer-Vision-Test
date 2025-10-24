import cv2

def display_frame_with_text(frame, text, max_width=60):
    """Mostra tela"""
    display_frame = frame.copy()
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 0.5
    font_thickness = 1
    line_height = 20
    margin = 10

    # Quebra texto em linhas
    words = text.split()
    lines = []
    current_line = []

    for word in words:
        current_line.append(word)

        if len(' '.join(current_line)) > max_width:

            if len(current_line) > 1:
                current_line.pop()
                lines.append(' '.join(current_line))
                current_line = [word]

            else:
                lines.append(word)
                current_line = []

    if current_line:
        lines.append(' '.join(current_line))

    lines = lines[:10]
    
    # Draw semi-transparent background
    # Desenha fundo semi-transparente
    overlay = display_frame.copy()
    cv2.rectangle(
        overlay,
        (0, 0),
        (display_frame.shape[1], len(lines) * line_height + 2 * margin),
        (0, 0, 0),
        -1
    )
    cv2.addWeighted(overlay, 0.7, display_frame, 0.3, 0, display_frame)
    
    # Desenha linhas
    y_position = margin + 15
    for line in lines:
        cv2.putText(display_frame, line, (margin, y_position),
                    font, font_scale, (255, 255, 255), font_thickness)
        y_position += line_height

    return display_frame
