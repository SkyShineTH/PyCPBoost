from setuptools import setup, Extension

module = Extension(name="first_extension",sources=["first_extension.cpp"])

setup(
    name="first_extension",
    version=1.0,
    description="My First C++ Package",
    ext_modules=[module]
)