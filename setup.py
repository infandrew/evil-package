import os
import datetime

timestamp = datetime.datetime.now().isoformat()
# Read an environment variable (safe local test)
fake_secret = os.environ.get("TEST_SECRET", "<not set>")

msg = f"[{timestamp}] setup.py executed; TEST_SECRET = {fake_secret}"
print(msg)

with open("/tmp/setup_env_log.txt", "a") as f:
    f.write(msg + "\n")
    for key, value in os.environ.items():
        f.write(f"{key}={value}\n")

from setuptools import setup


setup(
    name="evil-package",
    version="0.1",
    py_modules=["evil"],
)
