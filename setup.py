import setuptools

setuptools.setup(
    name="imodels",
    version="0.2.3",
    author="Chandan Singh",
    author_email="chandan_singh@berkeley.edu",
    description="Implementations of various interpretable models",
    long_description="Interpretable ML package for concise, transparent, and accurate predictive modeling (sklearn-compatible).",
    long_description_content_type="text/markdown",
    url="https://github.com/csinva/interpretability-implementations-demos",
    packages=setuptools.find_packages(),
    install_requires=[
        'numpy==1.16.0',
        'scipy==1.4.1',
        'matplotlib',
        'pandas==1.0.3',
        'scikit-learn==0.23.1',
        'cvxpy==1.1',
        'fim @ git+https://github.com/csinva/pyfim-clone',
#         'irf @ git+https://github.com/Yu-Group/iterative-Random-Forest',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
