#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Testing emlx2eml."""

import logging
import mimetypes
import unittest
import email
import emlx2eml

class Emlx2EmlTestCase(unittest.TestCase):
    """Unit tests for emlx2eml."""

    def test_extension_guesser_from_message(self):
        """Make sure guessed file extensions are correct."""

        INPUT="Content-Transfer-Encoding: base64\nContent-Disposition: inline;\n\tfilename=page-icon.jpg\nContent-Type: image/jpeg;\n\tname=page-icon.jpg\nX-Apple-Content-Length: 28187\nContent-Id: <page-icon>\n\n"
        input = email.message_from_string(INPUT)
        output = emlx2eml.get_filename(input)
        self.assertEqual(output, 'page-icon.jpg')

    def test_extension_guesser(self):
        """Make sure guessed file extensions are correct."""

        self.assertEqual(emlx2eml.guess_extension('image/jpeg'), 'Mail Attachment.jpg')
        self.assertEqual(emlx2eml.guess_extension('text/calendar'), 'Mail Attachment.ics')
        self.assertEqual(emlx2eml.guess_extension('image/png'), 'Mail Attachment.png')
        self.assertEqual(emlx2eml.guess_extension('image/x-png'), 'Mail Attachment')
        self.assertEqual(emlx2eml.guess_extension('image/gif'), 'Mail Attachment.gif')
        self.assertEqual(emlx2eml.guess_extension('message/rfc822'), 'Mail Attachment.eml')


if __name__ == '__main__':
    unittest.main()
