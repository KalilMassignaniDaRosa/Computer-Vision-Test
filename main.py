import sys
import cv2
from camera import CameraManager
from vision import VisionAnalyzer
from display import display_frame_with_text
from utils import (
    print_analysis_with_bars,
    print_menu,
    print_controls,
    print_status,
    print_separator,
)


def interactive_mode(camera: CameraManager, analyzer: VisionAnalyzer):
    """Modo interativo"""
    print("\n+------------------+")
    print("| INTERACTIVE MODE |")
    print("+------------------+\n")

    controls = {
        "SPACE": "Analyze current frame",
        "C": "Set custom prompt",
        "Q": "Quit"
    }
    print_controls(controls)

    last_analysis = "Press SPACE to analyze the image"
    custom_prompt = None

    try:
        while True:
            frame = camera.capture_frame()

            if frame is None:
                print_status("Error capturing frame", "error")
                break

            # Mostra o frame SEM texto sobreposto
            cv2.imshow("Gemini Vision - Interactive Mode", frame)
            key = cv2.waitKey(1) & 0xFF

            if key in (ord('q'), ord('Q')):
                print_status("Exiting interactive mode...", "info")
                break

            elif key in (ord('c'), ord('C')):
                print_separator()
                user_input = input("Enter your prompt (press Enter for default): ").strip()
                custom_prompt = user_input or None
                print_status(f"Prompt set: {custom_prompt or 'default'}", "success")

            elif key == ord(' '):
                print_separator()

                pil_img = camera.frame_to_pil(frame)
                analysis = analyzer.analyze_frame(pil_img, custom_prompt)
                last_analysis = analysis

                print_analysis_with_bars(analysis)

    finally:
        camera.release()
        cv2.destroyAllWindows()


def single_shot_mode(camera: CameraManager, analyzer: VisionAnalyzer):
    """Foto única"""
    print("\n+------------------+")
    print("| SINGLE SHOT MODE |")
    print("+------------------+\n")

    controls = {
        "SPACE": "Capture and analyze",
        "Q": "Quit"
    }
    print_controls(controls)

    try:
        while True:
            frame = camera.capture_frame()

            if frame is None:
                print_status("Error capturing frame", "error")
                break

            cv2.imshow("Gemini Vision - Single Shot", frame)
            key = cv2.waitKey(1) & 0xFF

            if key in (ord('q'), ord('Q')):
                print_status("Exiting single shot mode...", "info")
                break

            elif key == ord(' '):
                print_separator()
                print_status("Frame captured!", "success")

                pil_img = camera.frame_to_pil(frame)
                user_prompt = input("\nEnter your question (press Enter for default): ").strip()
                user_prompt = user_prompt or None

                analysis = analyzer.analyze_frame(pil_img, user_prompt)
                print_analysis_with_bars(analysis)

                print_status("Press SPACE for a new analysis or Q to quit", "info")

    finally:
        camera.release()
        cv2.destroyAllWindows()


def main():
    """Entry point do Gemini Vision App"""
    try:
        camera = CameraManager()
        camera.initialize()
        analyzer = VisionAnalyzer()

        menu_options = [
            "Interactive Mode",
            "Single Shot Mode",
            "Exit"
        ]
        print_menu(menu_options)

        choice = input("Your choice: ").strip()
        print_separator(False)

        if choice == '1':
            interactive_mode(camera, analyzer)
        elif choice == '2':
            single_shot_mode(camera, analyzer)
        elif choice == '3':
            print_status("Exiting application...", "info")
            sys.exit(0)
        else:
            print_status("Invalid option!", "error")

    except KeyboardInterrupt:
        print_status("\nApplication interrupted by user", "info")
        sys.exit(0)

    except Exception as e:
        print_status(f"Fatal error: {str(e)}", "error")
        sys.exit(1)


if __name__ == "__main__":
    main()