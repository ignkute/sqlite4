from setuptools import setup

readme = open("./README.md", "r")

setup(
    name='sqlite4',
    packages=['sqlite4'],  # this must be the same as the name above
    version='0.1',
    description='Modifies SQLite3 Syntax',
    long_description=readme.read(),
    long_description_content_type='text/markdown',
    author='kute#0001',
    author_email='',
    # use the URL to the github repo
    url='https://github.com/ignkute/sqlite4',
    download_url='https://github.com/ignkute/sqlite4/tarball/0.1',
    keywords=['database'],
    classifiers=[ ],
    license='MIT',
    include_package_data=True
)