###############################################################################
#
# The MIT License (MIT)
#
# Copyright (c) Tavendo GmbH
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
###############################################################################

from __future__ import absolute_import

import sys

from autobahn import wamp
from autobahn.wamp import message
from autobahn.wamp import exception
from autobahn.wamp import protocol

if sys.version_info < (2, 7):
    # noinspection PyUnresolvedReferences
    import unittest2 as unittest
else:
    # from twisted.trial import unittest
    import unittest


class TestPeerExceptions(unittest.TestCase):

    def test_exception_from_message(self):
        session = protocol.BaseSession()

        @wamp.error(u"com.myapp.error1")
        class AppError1(Exception):
            pass

        @wamp.error(u"com.myapp.error2")
        class AppError2(Exception):
            pass

        session.define(AppError1)
        session.define(AppError2)

        # map defined errors to user exceptions
        emsg = message.Error(message.Call.MESSAGE_TYPE, 123456, u'com.myapp.error1')
        exc = session._exception_from_message(emsg)
        self.assertIsInstance(exc, AppError1)
        self.assertEqual(exc.args, ())

        emsg = message.Error(message.Call.MESSAGE_TYPE, 123456, u'com.myapp.error2')
        exc = session._exception_from_message(emsg)
        self.assertIsInstance(exc, AppError2)
        self.assertEqual(exc.args, ())

        # map undefined error to (generic) exception
        emsg = message.Error(message.Call.MESSAGE_TYPE, 123456, u'com.myapp.error3')
        exc = session._exception_from_message(emsg)
        self.assertIsInstance(exc, exception.ApplicationError)
        self.assertEqual(exc.error, u'com.myapp.error3')
        self.assertEqual(exc.args, ())
        self.assertEqual(exc.kwargs, {})

        emsg = message.Error(message.Call.MESSAGE_TYPE, 123456, u'com.myapp.error3', args=[1, 2, u'hello'])
        exc = session._exception_from_message(emsg)
        self.assertIsInstance(exc, exception.ApplicationError)
        self.assertEqual(exc.error, u'com.myapp.error3')
        self.assertEqual(exc.args, (1, 2, u'hello'))
        self.assertEqual(exc.kwargs, {})

        emsg = message.Error(message.Call.MESSAGE_TYPE, 123456, u'com.myapp.error3', args=[1, 2, u'hello'], kwargs={u'foo': 23, u'bar': u'baz'})
        exc = session._exception_from_message(emsg)
        self.assertIsInstance(exc, exception.ApplicationError)
        self.assertEqual(exc.error, u'com.myapp.error3')
        self.assertEqual(exc.args, (1, 2, u'hello'))
        self.assertEqual(exc.kwargs, {u'foo': 23, u'bar': u'baz'})

    def test_message_from_exception(self):
        session = protocol.BaseSession()

        @wamp.error(u"com.myapp.error1")
        class AppError1(Exception):
            pass

        @wamp.error(u"com.myapp.error2")
        class AppError2(Exception):
            pass

        session.define(AppError1)
        session.define(AppError2)

        exc = AppError1()
        msg = session._message_from_exception(message.Call.MESSAGE_TYPE, 123456, exc)

        self.assertEqual(msg.marshal(), [message.Error.MESSAGE_TYPE, message.Call.MESSAGE_TYPE, 123456, {}, "com.myapp.error1"])


if __name__ == '__main__':
    unittest.main()
