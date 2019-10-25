import setuptools
from distutils.core import setup

INSTALL_REQUIREMENTS = ['requests']

setup(
    name = 'bitpreco',
    description = 'A Python wrapper for Bitpreco API',
    version = '0.2.0',
    packages = ['bitpreco'],
    author = 'Romeu Campos',
    author_email = 'romeu.campos@hotmail.com',
    url = 'https://github.com/romeucampos/python-bitpreco-api',
    download_url = 'https://github.com/romeucampos/python-bitpreco-api/archive/master.zip',
    keywords = ['bitcoin', 'bitpreco', 'trade', 'orderbook', 'cryptocurrency','ticker'],
    install_requires=INSTALL_REQUIREMENTS,
    classifiers = [
        'Development Status :: Beta',
        'Environment :: Console',
        'Intended Audience :: Customer Service',
        'Intended Audience :: Financial and Insurance Industry',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities'
    ]
)
