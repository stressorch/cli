"""Tests for our `skele hello` subcommand."""


from subprocess import PIPE, Popen as popen
from unittest import TestCase


class TestK8s(TestCase):
    def test_returns_multiple_lines(self):
        output = popen(['stressorch', 'k8s'], stdout=PIPE).communicate()[0]
        lines = output.split('\n')
        self.assertTrue(len(lines) != 1)

    def test_returns_hello_world(self):
        output = popen(['stressorch', 'hello'], stdout=PIPE).communicate()[0]
        self.assertTrue('Hello from k8s!' in output)
