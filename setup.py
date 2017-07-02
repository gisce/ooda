from setuptools import setup, find_packages


setup(
    name='ooda',
    version='0.1.0-dev',
    packages=find_packages(),
    url='https://github.com/gisce/ooda',
    license='GPL-2',
    install_requires=['psycopg2'],
    author='GISCE-TI, S.L.',
    author_email='devel@gisce.net',
    description='OpenOriented Data Access'
)
