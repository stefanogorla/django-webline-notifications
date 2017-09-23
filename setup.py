from io import open
from distutils.core import setup

long_description = open('README.md', encoding="utf-8").read()

install_requires = [
    'django>=1.8'
]

setup(
    name='django-webline-notifications',
    version='0.1',
    packages=['webline_notifications'],
    include_package_data=True,
    url='https://github.com/stefanogorla/django-webline-notifications',
    license='GNU General Public License (GPL)',
    author='stefano gorla',
    author_email='stefano.gorla@mail.polimi.it',
    description='Fork of django-webline-notifications by Alireza Molaee',
    long_description=long_description,
    install_requires=install_requires,
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ],
)
