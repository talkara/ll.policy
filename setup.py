from setuptools import find_packages
from setuptools import setup


setup(
    name='ll.policy',
    version='0.1',
    description="Turns Plone Site into LL site.",
    long_description=open("README.rst").read(),
    classifiers=[
        "Framework :: Plone",
        "Framework :: Plone :: 4.2",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7"],
    keywords='',
    author='Taito Horiuchi',
    author_email='taito.horiuchi@abita.fi',
    url='http://www.ll.fi',
    license='Non-free',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['ll'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'abita.development',
        'hexagonit.testing',
        'll.theme',
        'setuptools',
        'z3c.autoinclude',
        'zope.i18nmessageid'],
    entry_points="""
    # -*- Entry points: -*-

    [z3c.autoinclude.plugin]
    target = plone
    """)
