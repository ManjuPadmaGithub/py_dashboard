from setuptools import setup, find_packages

setup(
    name="my_app",                  # package name
    version="0.1",                  # version number
    packages=find_packages(),       # auto-detect packages
    install_requires=[              # dependencies
        "streamlit",
        "pandas",
        "plotly"
    ],
    entry_points={
        "console_scripts": [
            "my_app=my_app.main:run_app"  # command-line entry point
        ]
    },
)