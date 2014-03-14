# coding=utf-8
from django.test import SimpleTestCase as TestCase
from django_sae.utils.decorators import retry


class DecoratorsTest(TestCase):
    n = 0

    @staticmethod
    def handle_error(exception):
        print exception

    def test_retry(self):
        @retry(3, hook=self.handle_error)
        def retry_me():
            self.n += 1
            raise Exception(u'exception in try %s' % self.n)

        self.assertRaises(Exception, retry_me)
        self.assertEqual(self.n, 3)







