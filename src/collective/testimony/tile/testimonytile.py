# -*- coding: utf-8 -*-

from embeddify import Embedder
from plone.tiles.tile import Tile
from random import randint


def get_random_testimony(context, video_only=False):
    query = {}
    query['in_the_random_testimony'] = True
    if video_only:
        query['is_video'] = True
    brains = context.portal_catalog(query)
    if not brains:
        return None
    brain = brains[randint(0, len(brains) - 1)]
    return brain.getObject()


class TestimonyTile(Tile):

    elected_testimony = None
    video_only = False

    @property
    def available(self):
        return self.testimony is not None

    @property
    def testimony(self):
        if self.elected_testimony is None:
            self.elected_testimony = get_random_testimony(
                self.context,
                video_only=self.video_only,
            )
        return self.elected_testimony


class TextualTile(TestimonyTile):

    def get_value(self):
        return {
            'url': self.testimony.absolute_url(),
            'text': self.testimony.description,
        }


class VideoTile(TestimonyTile):

    video_only = True

    def get_value(self):
        return {
            'url': self.testimony.absolute_url(),
            'video_url': self.testimony.url,
            'video_description': self.testimony.video_transcript,
        }

    def get_embed_link(self, url):
        embedder = Embedder()
        return embedder(url, params=dict(autoplay=False))
