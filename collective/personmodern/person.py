# -*- coding: utf-8 -*-
from zope.interface import Interface, implements
from plone.dexterity.content import Item, Container
from plone.app.content.interfaces import INameFromTitle
from plone.dexterity.utils import safe_unicode
from zope.interface import provider
from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from plone.app.content.interfaces import INameFromTitle
from collective.personmodern import MessageFactory as _
from zope import schema

class INameFromPersonNames(INameFromTitle):
    def title():
        """Return a processed title"""

class NameFromPersonNames(object):
    implements(INameFromPersonNames)

    def __init__(self, context):
        self.context = context

    def generate_title(self):
        name = getattr(self.context, 'name', None)
        if name:
            # this is a CMF accessor, so should return utf8-encoded
            if isinstance(name, unicode):
                return name.encode('utf-8')
            return name
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
        name = getattr(self, 'name', None)
        if name:
            # this is a CMF accessor, so should return utf8-encoded
            if isinstance(name, unicode):
                return name.encode('utf-8')
            return name
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



@provider(IFormFieldProvider)
class ICreator(model.Schema):
    """Interface for Exhibition behavior."""

    # exhibition fieldset
    model.fieldset(
        'creator',
        label=_(u'Creator', default=u'Creator'),
        fields=['place_of_birth', 'place_of_death', "birth_date_start", "birth_date_end", "death_date_start", "death_date_end", "persistent_url"],
    )

    place_of_birth = schema.TextLine(
        title=_(u'place_of_birth', default=u'Place of birth'),
        required=False
    )

    place_of_death = schema.TextLine(
        title=_(u'place_of_death', default=u'Place of death'),
        required=False
    )

    birth_date_start = schema.TextLine(
        title=_(u'birth_date_start', default=u'Birth data start'),
        required=False
    )

    birth_date_end = schema.TextLine(
        title=_(u'birth_date_end', default=u'Birth date end'),
        required=False
    )

    death_date_start = schema.TextLine(
        title=_(u'death_date_start', default=u'Death date start'),
        required=False
    )

    death_date_end = schema.TextLine(
        title=_(u'death_date_end', default=u'Death date end'),
        required=False
    )

    persistent_url = schema.TextLine(
        title=_(u'persistent_url', default=u'Persistent url'),
        required=False
    )



    

