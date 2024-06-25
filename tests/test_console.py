#!/usr/bin/python3
"""Tests for the console"""
import unittest
from unittest.mock import patch
import os
from io import StringIO
import console
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """Series of tests for console"""

    @classmethod
    def setClass(cls):
        """Setup for the tests"""
        cls.consol = HBNBCommand()

    @classmethod
    def tearclass(cls):
        """Tears down at the end of the test"""
        del cls.consol

    def tearClass(self):
        """Remove temp file.json created"""
        if (os.getenv('HBNB_TYPE_STORAGE') != 'db'):
            try:
                os.remove("file.json")
            except Exception:
                pass

    def test_docstring_console(self):
        """Check for docstrings"""
        self.assertIsNotNone(console.__doc__)
        self.assertIsNotNone(HBNBCommand.emptyline.__doc__)
        self.assertIsNotNone(HBNBCommand.do_quit.__doc__)
        self.assertIsNotNone(HBNBCommand.do_create.__doc__)
        self.assertIsNotNone(HBNBCommand.do_show.__doc__)
        self.assertIsNotNone(HBNBCommand.do_count.__doc__)
        self.assertIsNotNone(HBNBCommand.do_all.__doc__)
        self.assertIsNotNone(HBNBCommand.do_destroy.__doc__)
        self.assertIsNotNone(HBNBCommand.do_EOF.__doc__)
        self.assertIsNotNone(HBNBCommand.do_update.__doc__)

    def test_emptyline(self):
        """Test for empty line"""
        with patch('sys.stdout', new=StringIO()) as file:
            self.consol.onecmd("\n")
            self.assertEqual('', file.getvalue())


if __name__ == "__main__":
    unittest.main()
