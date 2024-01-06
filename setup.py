import setuptools
with open("README.md", 'r', encoding = 'utf-8') as f:
    long_description = f.read()

__version__ = '0.0.0'

REPO_NAME = 'TEXT-SUMMARIZER'
AUTHOT_USER_NAME = 'Ramesh'
SRC_REPO = 'TextSummarizer'
AUTHOR_EMAIL = 'ramesh.pandey.1015@gmail.com'


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOT_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description='A small python package for NLP app',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/{AUTHOR_USER_NAME/{REPO_NAME}",
    project_urls={
        "Bug Tracker": "https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
        "Source Code": "https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    },
    package_dir= {'':"src"},
    packages=setuptools.find_packages(where='src'),
    )