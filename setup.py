from setuptools import setup


setup(
    name='mkzbomb',
    version='1.0.2',
    description='ZipBomb builder',
    long_description=open("README.md", "r").read(),
    long_description_content_type='text/markdown',
    url='https://github.com/jacopodl/mkzbomb',
    author='Jacopo De Luca',
    author_email='jacopo.delu@gmail.com',
    license='GNU General Public License v3',
    keywords='zbomb zipbomb zip bomb hacking-tool',
    packages=['mkzbomb'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Programming Language :: Python :: 3'
    ],
    entry_points={
        'console_scripts': ['mkzbomb=mkzbomb.mkzbomb:main']
    }
)
