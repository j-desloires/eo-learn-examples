import os
from setuptools import setup, find_packages


def parse_requirements(file):
    return sorted(
        (
            {
                line.partition('#')[0].strip()
                for line in open(os.path.join(os.path.dirname(__file__), file))
            }
            - set('')
        )
    )


setup(
    name='eo-flow',
    python_requires='>=3.7',
    version='1.2.0',
    description='Tensorflow wrapper built for prototyping and deploying earth observation deep models.',
    author='Sinergise EO research team',
    author_email='eoresearch@sinergise.com',
    packages=find_packages(),
    install_requires=parse_requirements('requirements.txt'),
    extras_require={
        'DEV': parse_requirements('requirements-dev.txt')
    }
)
