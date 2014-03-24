#!/usr/bin/env python

from reviewboard.extensions.packaging import setup


PACKAGE = 'rbscreenshotminimal'
VERSION = '0.2'

setup(
    name=PACKAGE,
    version=VERSION,
    description='Remove all UI unrelated to image attachment review',
    url='',
    author='Matthew N.',
    author_email='',
    maintainer='',
    maintainer_email='',
    packages=['rbscreenshotminimal'],
    install_requires=[
        'ReviewBoard>=1.8alpha0.dev',
    ],
    entry_points={
        'reviewboard.extensions': [
            'rbscreenshotminimal = rbscreenshotminimal.extension:RBScreenshotMinimalExtension',
        ],
    },
    package_data={
        'rbscreenshotminimal': [
            'static/css/*',
            'static/js/*',
        ]
    },
)
