from distutils.core import setup
REQUIRES = [
    'structlog',
    'records',
    'allure-pytest'
]

setup(
    name='db_client',
    version='0.0.1',
    packages=['db_client'],
    url='https://github.com/AlexStark9/db_client.git',
    license='MIT',
    author='Alex Stark',
    author_email='-',
    install_requires=REQUIRES,
    description='database client with allure and loger'
)
