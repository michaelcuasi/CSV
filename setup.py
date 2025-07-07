from setuptools import find_packages, setup

setup(
  name='mcqgenerator',
  version='0.0.1',
  author='michael cuasi',
  author_email='michaelcuasi@gmail.com',
  intall_requires=["openai", "langchain", "streamlit", "python-dotenv", "PyPDF2"],
  packages=find_packages()
)