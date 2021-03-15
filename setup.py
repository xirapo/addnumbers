# creating addnumbers
from setuptools import setup as s, find_packages
from setuptools.command.install import install
import os
import atexit

here = os.path.abspath(os.path.dirname(__file__))
VERSION = '0.1'
DESCRIPTION = 'Testing packages'
pck_url ='https://github.com/xirapo/add2numbers.git'

class PostInstall(install):

    def run(self):
        self._post_install()
        install.run(self)

    def _post_install(self):
        return print("Running post install script")



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
    cmdclass={'install':PostInstall},
)
