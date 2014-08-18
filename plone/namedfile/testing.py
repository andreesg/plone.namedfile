from StringIO import StringIO
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer

import PIL.Image
import os


# TODO: Should better use layer from plone.testing, but first get it working.
class NamedFileLayer(PloneSandboxLayer):
    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, conf_ctx):
        # Load ZCML
        import plone.namedfile
        self.loadZCML(package=plone.namedfile, context=conf_ctx)

NAMEDFILE_FIXTURE = NamedFileLayer()
NAMEDFILE_INTEGRATION_TESTING = IntegrationTesting(
    bases=(NAMEDFILE_FIXTURE,),
    name="NamedFile:Integration"
)


def getFile(filename):
    """ return contents of the file with the given name """
    filename = os.path.join(os.path.dirname(__file__), 'tests', filename)
    return open(filename, 'r')


class ImageTestMixin(object):
    def assertImage(self, data, format, size):
        image = PIL.Image.open(StringIO(data))
        self.assertEqual(image.format, format)
        self.assertEqual(image.size, size)


#from plone.testing import Layer
#from plone.testing import z2
#
#class NamedFileLayer(Layer):
#    defaultBases = (z2.STARTUP,)
#
#    def setUpZope(self, app, conf_ctx):
#        import plone.namedfile
#        self.loadZCML(package=plone.namedfile, context=conf_ctx)
#
#NAMEDFILE_FIXTURE = NamedFileLayer()
#NAMEDFILE_INTEGRATION_TESTING = z2.IntegrationTesting(
#    bases=(NAMEDFILE_FIXTURE,),
#    name="NamedFile:Integration"
#)
