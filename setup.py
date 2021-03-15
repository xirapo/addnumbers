# creating addnumbers
from setuptools import setup as s, find_packages
from setuptools.command.install import install
import os
import atexit

here = os.path.abspath(os.path.dirname(__file__))
VERSION = '0.1'
DESCRIPTION = 'Testing packages'
pck_url ='https://github.com/xirapo/add2numbers.git'

def test():
    return print("hello")

test()

class PostInstall(install):
    def run_script(self):
        self.print("Post Installs Script...")



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
    cmdclass={'install':PostInstall}
)
