from setuptools import setup, Extension

module = Extension(name="PyCPBoost",sources=["PyCPBoost.cpp"])

setup(
    name="PyCPBoost",
    version=1.0,
    description="My First C++ Package",
    ext_modules=[module]
)