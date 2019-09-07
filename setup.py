import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="andromeda",
    version="1.0.0",
    author="Kaleb McKinney",
    description="Quickly create large amounts of unique serial numbers.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mckkaleb/andromeda",
    packages=setuptools.find_packages(),
    python_requires='>=3.4',
)