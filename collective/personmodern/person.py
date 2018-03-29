# -*- coding: utf-8 -*-
from zope.interface import Interface, implements
from plone.dexterity.content import Item, Container
from plone.app.content.interfaces import INameFromTitle
from plone.dexterity.utils import safe_unicode

from plone.app.content.interfaces import INameFromTitle

class INameFromPersonNames(INameFromTitle):
    def title():
        """Return a processed title"""

class NameFromPersonNames(object):
    implements(INameFromPersonNames)

    def __init__(self, context):
        self.context = context

    def generate_title(self):
        names_list = [getattr(self.context, 'firstname', None), getattr(self.context, 'middlename', None), getattr(self.context, 'lastname', None)]
        names = " ".join([name for name in names_list if name])

        names = ""

        extra = []
        if hasattr(self.context, 'nationality'):
            if self.context.nationality:
                extra.append(self.context.nationality)
        if hasattr(self.context, 'year'):
            if self.context.year:
                extra.append(self.context.year)

        extra_text = ', '.join(extra)

        if names and extra_text:
            final_text = "%s (%s)" %(names, extra_text)
            return final_text
        elif names and not extra_text:
            final_text = "%s" %(names)
            return final_text
        else:
            # this is a CMF accessor, so should return utf8-encoded
            if isinstance(self.context.title, unicode):
                return self.context.title.encode('utf-8')
            return self.context.title or ''

    @property
    def title(self):
        title = self.generate_title()
        if isinstance(title, unicode):
            return title
        return title


class IPerson(Interface):
    """  Interface for Person content type """

class Person(Container):
    """Customised person content class"""
    implements(IPerson)

    def generate_title(self):
        names = ""
        names_list = [getattr(self, 'firstname', None), getattr(self, 'middlename', None), getattr(self, 'lastname', None)]
        names = " ".join([name for name in names_list if name])

        extra = []
        if hasattr(self, 'nationality'):
            if self.nationality:
                extra.append(self.nationality)
        if hasattr(self, 'year'):
            if self.year:
                extra.append(self.year)

        extra_text = ', '.join(extra)

        if names and extra_text:
            final_text = "%s (%s)" %(names, extra_text)
            return final_text
        elif names and not extra_text:
            final_text = "%s" %(names)
            return final_text
        else:
            # this is a CMF accessor, so should return utf8-encoded
            if isinstance(self.title, unicode):
                return self.title.encode('utf-8')
            return self.title or ''

    def Title(self):
        title = self.generate_title()
        # this is a CMF accessor, so should return utf8-encoded
        if isinstance(title, unicode):
            return title
        return title

    def setTitle(self, title):
        # Set Dublin Core Title element - resource name.
        self.title = safe_unicode(title)


    

