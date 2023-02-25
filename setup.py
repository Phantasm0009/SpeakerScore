import os, sys
try:
    from setuptools import setup, find_packages
    use_setuptools = True
except ImportError:
    from distutils.core import setup
    use_setuptools = False

try:
    with open('README.rst', 'rt') as readme:
        description = '\n' + readme.read()
except IOError:
    # maybe running setup.py from some other dir
    description = ''

python_requires='>=3.6'
install_requires = [
    'rx>=3.0',
    'scipy>=1.0',
    'cyclotron>=1.2',
    'cyclotron-aiohttp>=1.0',
    'cyclotron-std>=1.0',
    'stt>=1.3',
    'pydantic>=1.9',
    'PyYAML>=6.0',
]

setup(
    name="SpeakerScore",
    version='1.0.0',
    url='https://github.com/Phantasm0009/SpeakerScore.git',
    license='MPL-2.0',
    description="server for mozilla deepspeech",
    long_description="Gives a graded holistic report of Speaking skills based upon 5 weighted criterion",
    long_description_content_type='text/x-rst',
    author='Sonoma Hacks Submission',
    author_email='atiwar0414@gmail.com',
    packages=find_packages(),
    install_requires=install_requires,
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Development Status :: 1 - Alpha',
        'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Artificial Intelligence'
    ],
    entry_points={
        'console_scripts': ['deepspeech-server=deepspeech_server.cli:main'],
    }
)
