# -*- coding: utf-8 -*-

from collective.testimony import _
from plone.app.textfield import RichText
from plone.app.z3cform.widget import AjaxSelectFieldWidget
from plone.autoform import directives
from plone.dexterity.browser import view
from plone.dexterity.content import Container
from plone.supermodel import model
from zope import schema
from zope.interface import implements


class ITestimony(model.Schema):
    """ITestimony"""

    domain = schema.TextLine(
        title=_(u"Domain"),
        required=False
    )

    url = schema.URI(
        title=_(u"URL address of the video"),
        required=False,
    )

    video_transcript = RichText(
        title=_(u"Video transcript"),
        required=False,
    )

    textual_testimony = RichText(
        title=_(u"Textual testimony"),
        required=False,
    )

    theme = schema.Tuple(
        title=u'Theme',
        value_type=schema.TextLine(),
        required=False,
        missing_value=(),
    )
    directives.widget(
        'theme',
        AjaxSelectFieldWidget,
        vocabulary='plone.app.vocabularies.Keywords'
    )

    in_the_random_testimony = schema.Bool(
        title=_(u"In the random testimony?"),
        required=True
    )

    first_name = schema.TextLine(
        title=_(u"First name"),
        required=False
    )

    function = schema.TextLine(
        title=_(u"Function"),
        required=False
    )

    age = schema.Int(
        title=_(u"Age"),
        required=False
    )


class Testimony(Container):
    implements(ITestimony)


class TestimonyView(view.DefaultView):
    """TestimonyView"""
