import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name="cloud_detector",
    version="0.1",
    # long_description_content_type="text/markdown",
    # url="https://github.com/jendas1/rooted-tree-classifier",
    author="Thonifho Muhali",
    author_email="tmuhali@student.wethinkcode.co.za",
    license="Unlicense",
    classifiers=[
        "License :: OSI Approved :: The Unlicense (Unlicense)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
    ],
    packages=["src"],
    include_package_data=True,
    install_requires=["cloudpathlib[azure]", "loguru", "tqdm", "typer"]
)
