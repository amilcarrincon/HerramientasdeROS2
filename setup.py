from setuptools import setup
from glob import glob
import os

package_name = 'Rincon_Charris_pkg'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
        (os.path.join('share', 'ament_index', 'resource_index', 'packages'), ['resource/' + package_name]),
        (os.path.join('share', package_name), ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='amilcar rincon',
    maintainer_email='amilcar.rincon@example.com',
    description='Paquete ROS 2 con launch',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={},
)
