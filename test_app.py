import flet as ft

def main(page: ft.Page):
    page.title = "Simple Test App"
    page.add(ft.Text("Hello, World!"))

print("Attempting to start Flet app...")
print("Python version:", ft.__version__)
try:
    ft.app(
        target=main,
        view=ft.AppView.DESKTOP,  # Explicitly set desktop view
        assets_dir="car_rental_app",  # Set assets directory
    )
except Exception as e:
    print(f"Error: {e}")
    print("Trying alternative approach...")
    try:
        # Try alternative port
        ft.app(
            target=main,
            port=0,  # Let the OS choose an available port
            view=ft.AppView.DESKTOP
        )
    except Exception as e:
        print(f"Alternative approach failed: {e}")
