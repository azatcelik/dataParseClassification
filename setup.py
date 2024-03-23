
import setuptools
 
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
 
setuptools.setup(
    name="dataParserCls",  
    version="0.1",
    author="azatcelik (Azat Çelik)",
    author_email="azatcellk@hotmail.com",
    description="Data parser for classification",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/azatcelik/dataParseClassification/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)