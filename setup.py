import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="simple-stopwatch-hrolfurgylfa",  # Replace with your own username
    version="1.0.0",
    author="Hrólfur Gylfason",
    author_email="hrolfurgylfa@protonmail.com",
    description="A small package to measure to time of different Python code.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hrolfurgylfa/SimpleStopwatch",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)