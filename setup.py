# setup.py file

from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="lambdata-dougscohen", # the name that you will install via pip
    version="1.0",
    author="Doug Cohen",
    author_email="doug-cohen@lambdastudents.com",
    description="package containing a function that converts a time in string to seconds, and a fucntion that converts state names to thier abbreviations",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md
    #file for long desc license="MIT",
    url="https://github.com/dougscohen/lambdata-dougscohen",
    #keywords="",
    packages=find_packages() # ["my_lambdata"]
)