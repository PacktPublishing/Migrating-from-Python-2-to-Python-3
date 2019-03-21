from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ 
    'aiohttp>=3.5',
]

setup_requirements = [ 
    'pytest-runner'
]

test_requirements = [ 
    'pytest'
]

setup(
    author="Ada Lovelace",
    author_email='myself@mail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
    ],
    description="My cool python project",
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    name='packt-calc',
    packages=find_packages(include=['packt_calc']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/PacktPublishing/Migrating-from-Python-2-to-Python-3/chapter08/packt-calc',
    version='0.1.0',
    zip_safe=True,
    entry_points={
        'console_scripts': ['packt-calc=packt_calc.cli:main'],
    }
)