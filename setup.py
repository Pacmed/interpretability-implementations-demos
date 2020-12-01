import setuptools

with open("readme.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="imodels",
    version="0.0.1",
    author="Chandan Singh",
    author_email="chandan_singh@berkeley.edu",
    description="Implementations of various interpretable models",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Pacmed/interpretability-implementations-demos",
    packages=setuptools.find_packages(),
    install_requires=[
        'numpy==1.16.0',
        'scipy==1.4.1',
        'matplotlib==3.1.2',
        'pandas==1.0.3',
        'scikit-learn==0.23.1',
        'fim @ git+https://github.com/Pacmed/pyfim-clone',                
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
