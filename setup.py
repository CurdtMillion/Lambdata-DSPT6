from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="U3M1_CurdtMillion", 
    version="3.0",
    author="Curtis Cecil",
    author_email="curtcecil@gmail.com",
    description="Unit 3 Package with PEP8, classes, mods, dockerfile and unittest",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/CurdtMillion/Lambdata-DSPT6",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
