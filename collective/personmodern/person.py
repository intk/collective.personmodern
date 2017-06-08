# -*- coding: utf-8 -*-
from zope.interface import Interface, implements
from plone.dexterity.content import Item, Container
from plone.app.content.interfaces import INameFromTitle
from plone.dexterity.utils import safe_unicode


class IPerson(Interface):
    """  Interface for Person content type """

class Person(Container):
    """Customised person content class"""
    implements(IPerson)

    def generate_title(self):
        names = ""
        if hasattr(self, 'firstname') and hasattr(self, 'lastname'):
            names = self.firstname + " " + self.lastname

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
        print "SET TITLE"
        # Set Dublin Core Title element - resource name.
        self.title = safe_unicode(title)


    

