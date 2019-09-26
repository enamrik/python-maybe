from setuptools import setup, find_packages


def read_file(filename):
    with open(filename) as f:
        return f.read()


setup(
    python_requires="~=3.7",
    name="python-maybe",
    version=read_file("./python_maybe/VERSION").strip(),
    description="Python maybe monad",
    long_description=read_file("README.md"),
    author="Kirmanie L Ravariere",
    author_email="enamrik@gmail.com",
    url="https://github.com/enamrik/python-maybe",
    license=read_file("LICENSE"),
    packages=find_packages(exclude=("tests", "outputs")),
    package_data={"python_maybe": ["VERSION", "*.txt", "*.yml", "*.template", "*.ini", "bin/**/*"]},
    include_package_data=True,
    install_requires=[],
    extras_require={
        'dev': ['pytest']
    },
)
