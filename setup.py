# creating addnumbers
from setuptools import setup as s, find_packages
import os


here = os.path.abspath(os.path.dirname(__file__))
VERSION = '0.1'
DESCRIPTION = 'Testing packages'
pck_url ='https://github.com/xirapo/add2numbers.git'

s(
    name='addnumbers',
    version=VERSION,
    description=DESCRIPTION,
    author='francisco garcia',
    url= pck_url,
    license='MIT',
    packages=find_packages(),
    install_requires=['m3u8','wheel'],
    zip_safe=False,
    entry_points={
        'console_scripts':[
            'post_install = post_install:install'
        ],
    },
)
