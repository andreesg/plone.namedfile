from Products.Five.testbrowser import Browser
from StringIO import StringIO
from Testing import ZopeTestCase as ztc
from plone.namedfile.testing import getFile
from zope.component import testing
from zope.configuration import xmlconfig
import PIL.Image


def setUp(self=None):
    testing.setUp()
    xmlconfig.xmlconfig(getFile('testing.zcml'))


class NamedFileLayer:
    setUp = classmethod(setUp)
    tearDown = classmethod(testing.tearDown)

try:
    from Testing.ZopeTestCase.layer import ZopeLite
except ImportError:
    pass
else:
    NamedFileLayer.__bases__ = (ZopeLite,)


class ImageTestMixin(object):

    def assertImage(self, data, format, size):
        image = PIL.Image.open(StringIO(data))
        self.assertEqual(image.format, format)
        self.assertEqual(image.size, size)


class NamedFileTestCase(ztc.TestCase, ImageTestMixin):
    layer = NamedFileLayer


class NamedFileFunctionalTestCase(
        ztc.Functional,
        ztc.ZopeTestCase,
        ImageTestMixin):
    layer = NamedFileLayer

    def getCredentials(self):
        return '%s:%s' % (ztc.user_name, ztc.user_password)

    def getBrowser(self, loggedIn=True):
        """ instantiate and return a testbrowser for convenience """
        browser = Browser()
        if loggedIn:
            auth = 'Basic %s' % self.getCredentials()
            browser.addHeader('Authorization', auth)
        return browser
