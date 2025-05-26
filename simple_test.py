import flet as ft
import sys

def main(page: ft.Page):
    # Create a simple UI
    page.title = "Simple Test"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    # Add a text widget
    text = ft.Text(
        value="Hello, World!",
        size=32,
        color=ft.colors.BLUE,
        weight=ft.FontWeight.BOLD,
    )
    
    # Add the text to the page
    page.add(text)

if __name__ == "__main__":
    print("Starting simple Flet test application...")
    try:
        ft.app(
            target=main,
            assets_dir="car_rental_app",
        )
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
