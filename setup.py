from setuptools import setup

setup(name="romexpander",
      version="0.4",
      author="Devon Meunier",
      author_email="devon.meunier@utoronto.ca",
      license="MIT",
      scripts=["romexpander.py"],
      description="NES ROM Expansion script compatible with DvD's " \
                  "ROM Expander Pro.",
      long_description=open("README").read(),
      install_requires=[
          "docopt>=0.3.0",
      ],
)
