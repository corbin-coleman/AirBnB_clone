#!/usr/bin/python3
"""
unit test for Console
"""
import sys
from unittest import TestCase
from unittest.mock import create_autospec
from console import HBNBCommand

class TestConsole(TestCase):
    """ test case class for console """

    def test_always_true(self):
        """ always return true """
        return True

    def setUp(self):
        """ setting up objects """
        self.mock_stdin = create_autospec(sys.stdin)
        self.mock_stdout = create_autospec(sys.stdout)

    def create(self, server=None):
        """ create method using mock """
        return HBNBCommand(stdin=self.mock_stdin, stdout=self.mock_stdout)

    def test_quit(self):
        """ testing quit commmand """
        cli = self.create()
        self.assertRaises(SystemExit, quit)

    def test_help(self):
        """ testing help command """
        cli = self.create()
        self.assertFalse(cli.onecmd("help"))

    def test_emptyline(self):
        """ testing emptyline command """
        cli = self.create()
        self.assertFalse(cli.onecmd("emptyline"))

    def test_EOF(self):
        """ testing EOF command """
        cli = self.create()
        self.assertRaises(SystemExit)

if __name__ == '__main__':
    unittest.main()
