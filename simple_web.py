import flet as ft
from car_rental_app.localization.translations import translator, t

def main(page: ft.Page):
    page.title = "Car Rental App Test"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = ft.Colors.BLUE_GREY_50
    
    def change_language(e):
        lang = dropdown.value
        translator.set_language(lang)
        title.value = t("app.title")
        login_title.value = t("login.title")
        email_label.value = t("login.email_label")
        page.update()

    # Language dropdown
    dropdown = ft.Dropdown(
        value="en",
        options=[
            ft.dropdown.Option("en", "English"),
            ft.dropdown.Option("fr", "Français"),
            ft.dropdown.Option("ar", "العربية"),
        ],
        on_change=change_language,
        width=200,
        bgcolor=ft.Colors.WHITE,
    )

    # Text elements to show translations
    title = ft.Text(t("app.title"), size=32, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900)
    login_title = ft.Text(t("login.title"), size=24)
    email_label = ft.Text(t("login.email_label"), size=16)

    # Add elements to page
    page.add(
        ft.Container(
            content=ft.Column(
                controls=[
                    ft.Row([ft.Text("Select Language:"), dropdown], alignment=ft.MainAxisAlignment.CENTER),
                    title,
                    login_title,
                    email_label,
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20,
            ),
            padding=50,
            bgcolor=ft.Colors.WHITE,
            border_radius=10,
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=15,
                color=ft.Colors.BLUE_GREY_100,
            ),
        )
    )

if __name__ == "__main__":
    print("Starting Flet web application on port 8000...")
    ft.app(target=main, view=ft.WEB_BROWSER, port=8000)
