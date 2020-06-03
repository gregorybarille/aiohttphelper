import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="aiohttphelper", # Replace with your own username
    version="1.0.8",
    author="Gregory Barillé",
    author_email="contact@gregorybarille.io",
    description="Simple wrapper for aiohttp. Designed for my own use but might be useful to others.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gregorybarille/aiocalls",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=["aiohttp[speedups]==3.6.2"]
)