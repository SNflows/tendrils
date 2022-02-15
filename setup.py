import setuptools
import tendrils

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='tendrils',
    version=tendrils.__version__,
    author="Emir Karamehmetoglu, Rasmus Handberg",
    description="Tendrils: API for accessing flows pipeline and data products.",
    long_description=long_description,
    packages=setuptools.find_packages(),
    license="LICENSE",
    classifiers=["Programming Language :: Python :: 3",
                 "License :: OSI Approved :: GNU GENERAL PUBLIC LICENSE",
                 "Operating System :: OS Independent"],
    python_requires='>=3.8',
    install_requires=['numpy',
                      'astropy',
                      'requests',
                      'tqdm',
                      ],

)
