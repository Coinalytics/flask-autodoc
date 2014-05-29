"""
Flask-Autodoc
-------------

Flask autodoc automatically creates an online documentation for your flask application.
"""
from setuptools import setup

def readme():
    with open('README') as f:
        return f.read()


setup(
    name='fork of Flask-Autodoc for Coinalytics',
    version='0.1.1',
    url='http://github.com/coinalytics/flask-autodoc',
    license='MIT',
    author='Bill Gleim',
    author_email='bill@coinalytics.co',
    description='API Documentation generator for Coinalytics flask-based API server',
    long_description=readme(),
    #py_modules=['flask_autodoc'],
    # if you would be using a package instead use packages instead
    # of py_modules:
    packages=['flask_autodoc'],
    package_data={'flask_autodoc': ['templates/autodoc_default.html']},
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    test_suite =  'tests.test_autodoc',
)
