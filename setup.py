from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="car_rental_app",
    version="1.0.0",
    author="BlackboxAI",
    description="A multilingual car rental management system",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "flet>=0.21.0",
        "reportlab>=4.0.0",
    ],
    package_data={
        'car_rental_app': [
            'localization/*.json',
            'localization/*.py',
            'fonts/*.ttf',
        ],
    },
    entry_points={
        'console_scripts': [
            'car-rental-app=car_rental_app.main:main',
        ],
    },
    python_requires='>=3.8',
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
)
