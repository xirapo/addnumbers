# creating package
from setuptools import setup as s, find_packages

s(
    name='add_2_numbers',
    version='0.0.1',
    description='Testing packages',
    author='francisco garcia',
    url='https://github.com/xirapo/add2numbers.git',
    license='MIT',
    packages=find_packages(),
    zip_safe=False
)
