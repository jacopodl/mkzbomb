from setuptools import setup

setup(
    name='mkzbomb',
    version='1.0.1',
    description='ZipBomb builder',
    url='https://github.com/jacopodl/mkzbomb',
    author='Jacopo De Luca',
    author_email='jacopo.delu@gmail.com',
    license='GNU General Public License v3.0',
    keywords='zbomb zipbomb zip bomb hacking-tool',
    packages=['mkzbomb'],
    entry_points={
        'console_scripts': ['mkzbomb=mkzbomb.mkzbomb:main']
    }
)
