import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

required = ['requests>=0.11.2',
            'requests-oauth2>=0.1.1']

setup(
    name = 'basecamp-next',
    version = '0.0.1',
    author = 'Rimvydas Naktinis',
    author_email = 'naktinis@gmail.com',
    description = ('Wrapper for Basecamp Next.'),
    license = "MIT",
    keywords = "basecamp bcx api",
    url = 'https://github.com/nous/basecamp-next',
    packages=['basecampx'],
    install_requires=required,
    long_description=read('README.md'),
    include_package_data = True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Bug Tracking',
    ],
)