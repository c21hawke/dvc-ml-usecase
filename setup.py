from setuptools import setup

with open("README.md","r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="src",
    version="0.0.1",
    author="c21hawke",
    description="A small package for dvc ml pipeline demo",
    Long_description=long_description,
    Long_description_content_type="text/markdown",
    url="https://github.com/chandrareddytiyyagura/dvc-ml-usecase",
    author_email="c21hawke@gmail.com",
    packages=["src"],
    python_requires=">=3.7",
    install_reqires=[
        'dvc',
        'pandas',
        'scikit-learn'
    ]
)