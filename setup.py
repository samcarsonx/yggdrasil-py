from setuptools import setup
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
  name = 'yggdrasil-py',
  packages = ['yggdrasil'],
  version = '1.0.5',
  license='MIT',
  description = 'Python wrapper for Mojang\'s Yggdrasil authentication service.',
  long_description=long_description,
  long_description_content_type='text/markdown',
  author = 'Sam Carson',
  author_email = 'me@samcarson.xyz',
  url = 'https://github.com/samcarsonx/yggdrasil-py',
  download_url = 'https://github.com/samcarsonx/yggdrasil-py/archive/1.0.5.tar.gz',
  keywords = ['mojang','yggdrasil','minecraft','scrolls','authentication'],
  install_requires = [],
  classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
  ],
)
