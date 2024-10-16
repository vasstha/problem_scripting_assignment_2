#manage the distribution process

from setuptools import setup, find_packages
#from setuptools.config.expand import entry_points

setup(
    name = "morning_greetings", #the package name
    version = "0.1",
    packages=find_packages(), #automatically find all packages in your project
    include_package_data=True, #include non-python files specified in MANIFEFST.in (if any)
    description="An application for sending personalized messages to list of friends",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    author="Vaskar Shrestha",
    author_email="vashr0444@oslomet.no",
    url="",
    install_requires = [

    ],
    entry_points={
        'console_scripts':[
            'morning_greetings = morning_greetings.main:main'  #points directly to the main function in main.py
        ],
    },
    python_requires = '>=3.6'
)