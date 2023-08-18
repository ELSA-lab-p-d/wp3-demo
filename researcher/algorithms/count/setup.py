from setuptools import setup, find_packages

setup(
    name='count_citizens',
    version="0.0.1",
    description='example algorithm to count citizens',
    url='https://github.com/ELSA-lab-p-d/wp3-demo',
    packages=find_packages(),
    python_requires='>=3.6',
    install_requires=[
        'vantage6-client>=3.10.4'
    ]
)