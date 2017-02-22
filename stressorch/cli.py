"""
stressorch

Usage:
  stressorch [--version] [--help] <command> [<args>...]

Options:
  -h --help                         Show this screen.

Commands:
  hello           Hello cmd line
  bye             Bye cmd line
  kube            Kube cli

Help:
  For help using this tool, please open an issue on the Github repository:
  https://github.com/julienstroheker/stressorch
"""


from . import __version__ as VERSION
from docopt import docopt
from inspect import getmembers, isclass


def main():
  """Main CLI entrypoint"""
  from . import commands

  args = docopt(__doc__, version=VERSION, options_first=True)

  config = None
  command_name = args["<command>"]
    
  argv = args['<args>']
  module = getattr(commands, command_name)
  commands = getmembers(module, isclass)
  command_class = None
  command = None
  for k, command_class in commands:
      if command_name.lower() in command_class.__name__.lower():
        command = command_class(config, argv)
  if command is None:
    raise Exception("Unrecognized command: " + command_name)
  command.run()
