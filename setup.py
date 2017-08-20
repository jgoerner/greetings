from setuptools import setup, find_packages

setup(name="jgoerner-greetings",
      version="1.0",
      description="A small weekend project without a deeper usage",
      packages=find_packages(),
      setup_requires=["pytest-runner"],
      tests_require=["pytest"]
      )
