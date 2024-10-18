from distutils.core import setup


def readme():
    with open('README.md') as f:
        return f.read()


setup(
    name="modforge",  # name of the package on PyPi
    version="0.0.0",  # version number
    description="Simple module forge",  # short textual description
    long_description=readme(),
    long_description_content_type='text/markdown',
    author="Antoine Magron",  # authors
    author_email='antoine.magron@epfl.ch',
    url="https://github.com/magantoine/modforge",  # link to the repo
    keywords="PRODUCTIVITY",  # can input a list of descriptive keywords TODO COMPLETE
    license="MIT",  # can chose licence TODO COMPLETE
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    entry_points={
        'console_scripts': [
            'senpy = senpy.cli:main'
        ]
    },
    install_requires=[
        "watchdog",
    ],
    packages=["modforge"],
    # link to the release
    # download_url="https://github.com/magantoine/senpy-package/archive/refs/tags/0.5.tar.gz"
)