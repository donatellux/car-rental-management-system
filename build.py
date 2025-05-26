import os
import shutil
import subprocess
import sys

def create_directories():
    """Create necessary directories for the build"""
    dirs = ['build', 'dist', 'assets']
    for d in dirs:
        if not os.path.exists(d):
            os.makedirs(d)

def copy_assets():
    """Copy assets to the build directory"""
    # Create assets directory in dist
    dist_assets = os.path.join('dist', 'assets')
    if not os.path.exists(dist_assets):
        os.makedirs(dist_assets)

    # Copy fonts
    if os.path.exists('fonts'):
        for font in os.listdir('fonts'):
            if font.endswith('.ttf'):
                shutil.copy(
                    os.path.join('fonts', font),
                    os.path.join(dist_assets, font)
                )

    # Copy localization files
    dist_localization = os.path.join('dist', 'localization')
    if not os.path.exists(dist_localization):
        os.makedirs(dist_localization)
    
    if os.path.exists('localization'):
        for file in os.listdir('localization'):
            if file.endswith('.json') or file.endswith('.py'):
                shutil.copy(
                    os.path.join('localization', file),
                    os.path.join(dist_localization, file)
                )

def create_spec():
    """Create the PyInstaller spec file"""
    spec_content = """# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('assets', 'assets'),
        ('localization', 'localization'),
    ],
    hiddenimports=['flet'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='CarRentalApp',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
"""
    with open('CarRentalApp.spec', 'w') as f:
        f.write(spec_content)

def build():
    """Build the executable"""
    try:
        # Install requirements
        subprocess.run([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'], check=True)
        
        # Create directories and copy assets
        create_directories()
        copy_assets()
        
        # Create spec file
        create_spec()
        
        # Build the executable
        subprocess.run(['pyinstaller', 'CarRentalApp.spec', '--clean'], check=True)
        
        print("Build completed successfully!")
        print("Executable can be found in the 'dist' directory")
        
    except subprocess.CalledProcessError as e:
        print(f"Error during build process: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)

if __name__ == '__main__':
    build()
