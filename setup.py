import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='tendrils',
    version="0.0.1",
    author="Emir Karamehmetoglu, Rasmus Handberg",
    author_email="emirkmo@github.com",
    description="Tendrils: API for accessing flows pipeline and data products.",
    long_description=long_description,
    packages=setuptools.find_packages(),
    license="LICENSE.rst",
    url="https://github.com/SNFLOWS/tendrils",
    classifiers=["Programming Language :: Python :: 3",
                 "License :: OSI Approved :: GNU GPLv3 License",
                 "Operating System :: OS Independent",
                 "Topic :: Scientific/Engineering :: Astronomy"],
    python_requires='>=3.8',
    install_requires=['numpy',
                      'astropy',
                      'requests',
                      'tqdm',
                      ],
    package_data={"tendrils": ["utils/*.ini"]}  # include any .ini found in utils.
)
