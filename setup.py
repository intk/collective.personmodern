from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='collective.personmodern',
      version=version,
      description="Person content type",
      long_description=open("README.md").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='plone portlet content',
      author='Andre Goncalves',
      author_email='andre@intk.com',
      url='http://plone.org',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'plone.app.relationfield',
          'plone.z3cform',
          'zope.schema',
          'zope.interface',
          'zope.component',
          'collective.dexteritytextindexer',
          'plone.app.textfield',
          'plone.dexterity',
          'plone.browserlayer',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
