import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="MobileRoboticsGT",
    version="0.0.1",
    author="Robin Amsters",
    author_email="robin.amsters@kuleuven.be",
    description="A Files related to the (online) exercises sessions from the mobile robotics course at KU Leuven, campus group T",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/RobinAmsters/Mobile_Robotics_Exercises",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
