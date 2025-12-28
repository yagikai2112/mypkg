import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'mypkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
    ("share/ament_index/resource_index/packages", ["resource/mypkg"]),
    ("share/mypkg", ["package.xml"]),
    ("share/mypkg/launch", ["launch/cpu_monitor.launch.py"]),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Kaito Yagiuchi',
    maintainer_email='Yagisan-k@outlook.jp',
    description='a package for practice',
    license='BSD-3-Clause',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'cpu_monitor = mypkg.cpu_monitor_node:main',
            'resource_listener = mypkg.resource_listener:main',
        ],
    },
)
