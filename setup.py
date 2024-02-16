from setuptools import setup, find_packages

setup(
    name='num_to_words',
    version='1.0.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'num_to_words = num_to_words.converter:main'
        ]
    },
    install_requires=[],
    python_requires='>=3.6',
)
