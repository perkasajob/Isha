from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in isha/__init__.py
from isha import __version__ as version

setup(
	name="isha",
	version=version,
	description="Isha Foundation",
	author="Isha Foundation",
	author_email="perkasajob@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
