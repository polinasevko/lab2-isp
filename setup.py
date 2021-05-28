from platform import python_version_tuple


try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup


if python_version_tuple()[0] < "3":
    raise ValueError("Error python version. Need python3 and more")

setup(
    name="serializer",
    version="1.0",
    description="Function and base object json/yaml/pickle serializer",
    author="Sevko Polina",
    author_email="polinasevko24@gmail.com",
    packages=["serializer"],
    install_requires=["pyyaml"],
    entry_points={
        "console_scripts": ["serializer = console_utility:main"]
    }
)