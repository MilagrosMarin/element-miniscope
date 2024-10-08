#!/usr/bin/env python
from os import path
from setuptools import find_packages, setup
import urllib.request

pkg_name = "element_miniscope"
here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.md"), "r") as f:
    long_description = f.read()

with open(path.join(here, pkg_name, "version.py")) as f:
    exec(f.read())

with urllib.request.urlopen(
    "https://raw.githubusercontent.com/flatironinstitute/CaImAn/master/requirements.txt"
) as f:
    caiman_requirements = f.read().decode("UTF-8").split("\n")

caiman_requirements.remove("")
caiman_requirements.append("future")

setup(
    name=pkg_name.replace("_", "-"),
    version=__version__,  # noqa: F821
    description="Miniscope DataJoint Element",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="DataJoint",
    author_email="info@datajoint.com",
    license="MIT",
    url=f'https://github.com/datajoint/{pkg_name.replace("_", "-")}',
    keywords="neuroscience miniscope science datajoint",
    packages=find_packages(exclude=["contrib", "docs", "tests*"]),
    scripts=[],
    install_requires=[
        "datajoint>=0.13.0",
        "ipykernel>=6.0.1",
        "ipywidgets",
        "plotly",
        "opencv-python",
    ],
    extras_require={
        "caiman_requirements": [caiman_requirements],
        "caiman": ["caiman @ git+https://github.com/datajoint/CaImAn.git"],
        "elements": [
            "element-animal @ git+https://github.com/datajoint/element-animal.git",
            "element-event @ git+https://github.com/datajoint/element-event.git",
            "element-interface @ git+https://github.com/datajoint/element-interface.git",
            "element-lab @ git+https://github.com/datajoint/element-lab.git",
            "element-session @ git+https://github.com/datajoint/element-session.git",
        ],
        "tests": ["pytest", "pytest-cov", "shutils"],
    },
)
