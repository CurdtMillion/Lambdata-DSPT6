from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="U3M1_CurdtMillion", 
    version="2.5.2",
    author="Curtis Cecil",
    author_email="curtcecil@gmail.com",
    description="A small example package, v2.5.1 all funcs can be imported! README updtd",
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
