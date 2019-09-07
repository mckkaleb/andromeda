import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="andromeda",
    version="1.0.0-pr",
    author="Kaleb McKinney",
    description="Quickly create large amounts of unique serial numbers.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mckkaleb/andromeda",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GPL-3.0",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.4',
)