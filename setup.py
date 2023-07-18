from setuptools import setup


setup(
    name='assemblyqc',
    python_requires='>3.6.6',
    version='0.0.2',
    url='https://github.com/stephenshank/assemblyqc',
    download_url="https://github.com/stephenshank/assemblyqc/archive/v0.0.1.tar.gz",
    description='Quality control of assemblies',
    author='Stephen D. Shank',
    author_email='sshank314@gmail.com',
    maintainer='Stephen D. Shank',
    maintainer_email='sshank314@gmail.com',
    install_requires=[
        'biopython>=1.76',
        'xmltodict==0.13.0'
    ],
    packages=['assemblyqc'],
    entry_points={
        'console_scripts': [
            'regal = assemblyqc.regal:regal_cli',
            'dss_xml_cleaner = assemblyqc.xmlcleaner:cli',
            'xml_to_json = assemblyqc.xmltojson:cli',
            'dss_json_cleaner = assemblyqc.jsoncleaner:cli'
        ]
    },
    classifiers=[
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'License :: OSI Approved :: MIT License',
    ],
    include_package_data=True
)
