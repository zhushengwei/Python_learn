try:
    from setuptools import setup
except:
    from distutils import setup

config = {
    'description': 'My Project',
    'author': 'My Name',
    'url': 'URL to get it at.',
    'author_email': 'My email',
    'version': '0.1',
    'install_requires': ['nose'],
    'scripts': [],
    'name': 'projectname'
}

setup(**config)