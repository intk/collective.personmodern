# -*- coding: utf-8 -*-
from zope.component import getUtility
from plone.indexer.decorator import indexer
from person import IPerson

from plone.i18n.normalizer.interfaces import INormalizer
from plone.app.contenttypes.behaviors.collection import ICollection

@indexer(IPerson)
def person_priref(person):
    try:
        terms = []
        normalized_id = getUtility(INormalizer).normalize(person.priref)
        if normalized_id:
            terms.append(normalized_id)
        return terms
    except:
        return []

@indexer(IPerson)
def objects_count(person):
    try:
        brains = ICollection(person).results(batch=False)
        total = len(brains)
        total_value = "%s" %(str(total))
        return total_value
    except:
        return ""
    
    
