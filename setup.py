from setuptools import setup, find_packages

setup(
    name="heaper",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "typer>=0.9.0",
    ],
    entry_points={
        "console_scripts": [
            "heaper=libheaper.cli:app",
            "pushq=libheaper.cli:pushq_app",
            "popq=libheaper.cli:popq_app",
            "peekq=libheaper.cli:peekq_app",
        ],
    },
    python_requires=">=3.6",
)
