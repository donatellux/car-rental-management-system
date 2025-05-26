import json
import os
import sys

def get_resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller"""
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        # Get the directory where this file (translations.py) is located
        base_path = os.path.dirname(os.path.abspath(__file__))
    
    return os.path.join(base_path, relative_path)

class TranslationManager:
    def __init__(self):
        self.current_language = "en"  # Default language
        self.translations = {}
        self.supported_languages = ["en", "fr", "ar"]
        self._load_translations()

    def _load_translations(self):
        """Load all translation files"""
        for lang in self.supported_languages:
            file_path = get_resource_path(f"{lang}.json")
            try:
                with open(file_path, "r", encoding="utf-8") as file:
                    self.translations[lang] = json.load(file)
            except Exception as e:
                print(f"Error loading {lang} translations: {str(e)}")
                self.translations[lang] = {}

    def get_text(self, key_path, language=None):
        """
        Get translated text for a given key path
        Example: get_text("login.title") will return the title in current language
        """
        lang = language or self.current_language
        keys = key_path.split(".")
        value = self.translations.get(lang, {})
        
        for key in keys:
            if isinstance(value, dict):
                value = value.get(key, key)
            else:
                return key
        
        return value

    def set_language(self, language):
        """Change current language"""
        if language in self.supported_languages:
            self.current_language = language
            return True
        return False

    def get_current_language(self):
        """Get current language code"""
        return self.current_language

    def is_rtl(self):
        """Check if current language is RTL"""
        return self.current_language == "ar"

    def get_language_name(self, language_code):
        """Get language name in its native form"""
        language_names = {
            "en": "English",
            "fr": "Français",
            "ar": "العربية"
        }
        return language_names.get(language_code, language_code)

# Create a global instance
translator = TranslationManager()

# Shorthand function for getting translated text
def t(key_path):
    return translator.get_text(key_path)
