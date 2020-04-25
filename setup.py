import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="example-pkg-YOUR-USERNAME-HERE", # Replace with your own username
    version="0.1.0",
    author="Toan Phan",
    author_email="toanphan.cs@gmail.com",
    description="A minimal terminal progress bar for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)