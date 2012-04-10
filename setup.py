# -*- coding: utf-8 -*-
try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages  # noqa

from pecan_validictory import __version__

setup(
    name='pecan-validictory',
    version=__version__,
    description="""
    """,
    long_description=None,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: BSD License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python'
    ],
    keywords='',
    url='',
    author='Jonathan LaCour',
    author_email='jonathan (at) cleverdevil.org',
    license='MIT',
    install_requires=['pecan', 'validictory'],
    tests_require=['WebTest >= 1.3.1'],  # py3 compat
    test_suite='pecan_wtforms.tests',
    zip_safe=False,
    packages=find_packages(exclude=['ez_setup']),
    entry_points="""
    [pecan.extension]
    validictory = pecan_validictory
    """
)
