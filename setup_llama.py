"""Set up the package."""
import sys
from pathlib import Path

from setuptools import find_packages, setup

with open(Path(__file__).absolute().parents[0] / "llama_index" / "VERSION") as _f:
    __version__ = _f.read().strip()

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

install_requires = [
    "dataclasses_json",
    "langchain",
    "numpy",
    "openai>=0.26.4",
    "pandas",
    "tenacity<8.2.0",
]

# NOTE: if python version >= 3.9, install tiktoken
# else install transformers
if sys.version_info >= (3, 9):
    install_requires.extend(["tiktoken"])
else:
    install_requires.extend(["transformers"])

# upload duplicate package to pypi
setup(
    name="llama_index",
    version=__version__,
    # packages=find_packages(),
    packages=find_packages(include=["llama*"]),
    description="Interface between LLMs and your data.",
    install_requires=install_requires,
    long_description=long_description,
    license="MIT",
    url="https://github.com/jerryjliu/gpt_index",
    include_package_data=True,
    long_description_content_type="text/markdown",
)
