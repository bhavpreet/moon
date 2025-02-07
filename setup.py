from distutils.core import setup
from setuptools import setup, find_packages

# long_description
readme_path = "./README.md"
long_description = open(readme_path, 'r').read()

setup(
    name = 'moon',
    packages = find_packages(),
    version = '1.1.2',
    license='MIT',
    description = 'Gets moon visualizations courtesy of NASA/Ernie Wright',
    long_description_content_type="text/markdown",
    long_description = long_description,
    author = 'Sadie Parker',
    author_email = 'sadiemparker@gmail.com',
    url = 'https://github.com/spacerest/moon',
    download_url = 'https://github.com/spacerest/moon/archive/v_1_1_2.tar.gz',
    keywords = ['MOON', 'ART'],
    install_requires=[
        'numpy~=1.20.2',
        'opencv-python~=4.5.1.48',
        'matplotlib~=3.2.1',
    ],
    classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Other Audience',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
