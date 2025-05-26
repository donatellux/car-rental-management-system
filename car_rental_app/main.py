import flet as ft
from car_rental_app.localization.translations import translator, t
import os
import sys

def get_resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller"""
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        # Get the directory where this file (main.py) is located
        base_path = os.path.dirname(os.path.abspath(__file__))
    
    return os.path.join(base_path, relative_path)

class CarRentalApp:
    def __init__(self):
        self.page = None
        self.current_view = None
        self.init_complete = False
        self.email_field = None
        self.password_field = None
        self.error_text = None

    def initialize(self, page: ft.Page):
        self.page = page
        self.setup_page()
        self.init_complete = True
        self.show_login()

    def setup_page(self):
        """Initialize page settings"""
        self.page.title = t("app.title")
        self.page.theme_mode = ft.ThemeMode.LIGHT
        self.page.padding = 0
        self.page.spacing = 0
        self.page.window_width = 1200
        self.page.window_height = 800
        self.page.window_resizable = True
        self.setup_theme()

    def setup_theme(self):
        """Setup application theme"""
        self.page.theme = ft.Theme(
            color_scheme_seed="blue",
            visual_density=ft.ThemeVisualDensity.COMFORTABLE,
        )
        # Set font family that supports all three languages
        try:
            self.page.fonts = {
                "Noto": get_resource_path("fonts/NotoSans-Regular.ttf"),
                "NotoArabic": get_resource_path("fonts/NotoSansArabic-Regular.ttf")
            }
            print(f"Loading fonts from: {get_resource_path('fonts')}")
        except Exception as e:
            print(f"Warning: Could not load fonts: {e}")
            
        # Set default font family
        self.page.theme.font_family = "Noto"
        # Set background color for the entire page
        self.page.bgcolor = ft.colors.BLUE_GREY_50

    def create_language_dropdown(self):
        """Create language selection dropdown"""
        return ft.Dropdown(
            value=translator.get_current_language(),
            options=[
                ft.dropdown.Option(
                    key=lang,
                    text=translator.get_language_name(lang)
                ) for lang in translator.supported_languages
            ],
            on_change=self.change_language,
            width=150,
            border_radius=10,
            bgcolor=ft.colors.WHITE,
        )

    def change_language(self, e):
        """Handle language change"""
        translator.set_language(e.control.value)
        # Update UI text
        self.page.title = t("app.title")
        # Update font family and text direction based on language
        if translator.is_rtl():
            self.page.theme.font_family = "NotoArabic"
            self.page.rtl = True
        else:
            self.page.theme.font_family = "Noto"
            self.page.rtl = False
        # Update all text elements
        self.update_translations()
        self.page.update()

    def create_login_view(self):
        """Create login view controls"""
        self.email_field = ft.TextField(
            label=t("login.email_label"),
            width=300,
            text_align=ft.TextAlign.START,
            border_radius=10,
            bgcolor=ft.colors.WHITE,
        )
        self.password_field = ft.TextField(
            label=t("login.password_label"),
            password=True,
            can_reveal_password=True,
            width=300,
            border_radius=10,
            bgcolor=ft.colors.WHITE,
        )
        self.error_text = ft.Text(
            color=ft.colors.RED,
            size=12,
            visible=False
        )
        
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text(
                        t("login.title"),
                        size=32,
                        weight=ft.FontWeight.BOLD,
                        text_align=ft.TextAlign.CENTER,
                        color=ft.colors.BLUE_900,
                    ),
                    self.email_field,
                    self.password_field,
                    self.error_text,
                    ft.ElevatedButton(
                        text=t("login.login_button"),
                        width=300,
                        on_click=self.login,
                        style=ft.ButtonStyle(
                            shape=ft.RoundedRectangleBorder(radius=10),
                            color=ft.colors.WHITE,
                            bgcolor=ft.colors.BLUE,
                        ),
                    ),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20,
            ),
            padding=50,
            alignment=ft.alignment.center,
            border_radius=10,
            bgcolor=ft.colors.WHITE,
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=15,
                color=ft.colors.BLUE_GREY_100,
            ),
        )

    def show_login(self):
        """Display login page"""
        self.page.clean()
        self.page.add(
            ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Row(
                            controls=[
                                ft.Text(t("app.language")),
                                self.create_language_dropdown()
                            ],
                            alignment=ft.MainAxisAlignment.END,
                        ),
                        self.create_login_view()
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                padding=20,
            )
        )

    def login(self, e):
        """Handle login attempt"""
        email = self.email_field.value
        password = self.password_field.value
        
        # Basic validation (replace with actual authentication logic)
        if email == "admin@example.com" and password == "admin":
            # TODO: Navigate to dashboard
            pass
        else:
            self.error_text.value = t("login.invalid_credentials")
            self.error_text.visible = True
            self.page.update()

    def update_translations(self):
        """Update all text elements when language changes"""
        if self.email_field:
            self.email_field.label = t("login.email_label")
        if self.password_field:
            self.password_field.label = t("login.password_label")
        if self.error_text and self.error_text.visible:
            self.error_text.value = t("login.invalid_credentials")

def main(page: ft.Page):
    try:
        app = CarRentalApp()
        app.initialize(page)
    except Exception as e:
        print(f"Error initializing app: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    try:
        # Run in desktop mode without web server
        print("Starting application in desktop mode...")
        ft.app(target=main, view=None)
    except Exception as e:
        print(f"Error starting app: {e}", file=sys.stderr)
        sys.exit(1)
