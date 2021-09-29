import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

PROJECT_NAME ="Perceptron_pypi"
User_Name = "Nryreddy"

setuptools.setup(
    name=f"{PROJECT_NAME}-{User_Name}",
    version="0.0.1",
    author="NryReddy",
    description="An implementation of Perceptron",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/{User_Name}/{PROJECT_NAME}",
    project_urls={
        "Bug Tracker": "https://github.com/{User_Name}/{PROJECT_NAME}/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.7",
    install_requires=[
        "numpy",
        "tqdm"
    ]

)