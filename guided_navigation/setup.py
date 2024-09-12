from setuptools import find_packages, setup

package_name = 'guided_navigation'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='gdaniel',
    maintainer_email='gudanielf@gmail.com',
    description='Guided navigation project',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'multi_camera = scripts.multi_camera_subscriber:main'
        ],
    },
)
