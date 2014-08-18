import doctest
import unittest
from plone.testing import layered
from plone.namedfile.testing import NAMEDFILE_INTEGRATION_TESTING

tests = (
    '../usage.txt',
    '../handler.txt',
    '../marshaler.txt',
    '../utils.txt',
)


def test_suite():
    return unittest.TestSuite(
        [layered(doctest.DocFileSuite(f, optionflags=doctest.ELLIPSIS),
                 layer=NAMEDFILE_INTEGRATION_TESTING)
            for f in tests]
    )
