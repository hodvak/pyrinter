from setuptools import setup, find_packages

setup(
    name='py-printer',
    version='0.0.1a1',
    packages=find_packages(include=['py_printer', 'py_printer.*']),
    author='Hod Vaknin',
    license='MIT',

    description='python printer package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    project_urls={
        'Source': 'https://github.com/hodvak/py-printer'
    },

    install_requires=['pywin32'],

    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Environment :: Win32 (MS Windows)',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python :: 3'
    ]

)


