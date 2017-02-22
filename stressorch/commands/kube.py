"""

The K8s command

Usage:
  kube <command> [help] [options]

Commands:
  connect           Try to iniate the connexion to the cluster
  test              test

Options:
  --url=<url>       Url of the k8s proxy API : http://localhost:8001

Help:
  For help using this cli 
  https://github.com/julienstroheker/stressorch

"""
from .base import Base

from docopt import docopt
from inspect import getmembers, ismethod
from json import dumps

import requests


class Kube(Base):
  """Say hello, world from K8s !"""

  def run(self):
    args = docopt(__doc__, argv=self.options)
    self.args = args
    
    command = self.args["<command>"]
    result = None
    methods = getmembers(self, predicate = ismethod)
    for name, method in methods:
      if name == command:
        result = method()
        if result is None:
          result = command + " returned no results"
    if result:
      print(result)
    else:
      print("Unknown command: '" + command + "'")
      self.help()
    
  def help(self):
    print(__doc__)

  def test(self):
    args = self.args
    print('Hello from test')
    test = self.args["--test"]
    print(test)

  def connect(self):
    """
    Iniate connexion to the cluster
    """
    url = self.args["--url"]
    print(url)
    r = requests.get(url + '/api/v1')
    print(r.text)