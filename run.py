#!/usr/bin/env python3
"""
Run script for the Car Rental Management System.
This script provides a convenient way to start the application.
"""

import sys
from car_rental_app.main import main
import flet as ft

if __name__ == "__main__":
    try:
        # Try to run the app with default port 8000
        ft.app(target=main, port=8000, view=ft.WEB_BROWSER)
    except Exception as e:
        print(f"Error starting application: {e}", file=sys.stderr)
        # If port 8000 is busy, try running in desktop mode
        print("Attempting to run in desktop mode...")
        try:
            ft.app(target=main)
        except Exception as e:
            print(f"Failed to start application: {e}", file=sys.stderr)
            sys.exit(1)
