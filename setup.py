from setuptools import setup, find_packages

with open("README.md","r",encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="src",
    version="0.0.1",
    description="A small package for dvc ml pipeline demo",
    long_description=long_description,
    url="https://github.com/amanchauhan71/simple-dvc-project",
    author_email="amanchauhan7172@gmail.com",
    package_dir={"":"src"},
    packages=find_packages(where="src"),
    license="GNU",
    python_requires=">=3.6",
    install_requires= [
        'dvc',
        'dvc[gdrive]',
        'dvc[s3]',
        'pandas',
        'scikit-learn'
    ]
)