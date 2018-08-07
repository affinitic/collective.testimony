from random import randint

from embeddify import Embedder
from plone.tiles.tile import Tile


def get_data(context):
    brains = context.portal_catalog({'in_the_random_testimony': {'query': True}})
    brain = brains[randint(0, len(brains) - 1)]
    return brain.getObject()


class TextualTile(Tile):

    def get_value(self):
        data = get_data(self.context)
        return {'absolute_url': data.absolute_url(), 'text': data.textual_testimony}


class VideoTile(Tile):

    def get_value(self):
        data = get_data(self.context)
        return {'absolute_url': data.absolute_url(), 'url': data.url, 'video_description': data.video_transcript, }

    def get_embed_link(self, url):
        embedder = Embedder()
        return embedder(url, params=dict(autoplay=True))
