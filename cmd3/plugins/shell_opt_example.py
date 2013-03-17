import textwrap
from docopt import docopt
import inspect
import sys
import importlib

class shell_opt_example:

    def help_opt_example(self):
        """
        Usage:
               opt_example [-vr] [FILE] ...

        Process FILE and optionally apply correction to either left-hand side or
        right-hand side.

        Arguments:
          FILE        optional input file
          CORRECTION  correction angle, needs FILE, --left or --right to be present

        Options:
          -v       verbose mode
          -r       make report

        """
        print textwrap.dedent(self.help_opt_example.__doc__)

    @staticmethod
    def _get_doc_args(help,args):
        arguments = docopt(textwrap.dedent(help.__doc__), argv=args)
        return arguments

    # def _get_class(self,meth):
    #    for cls in inspect.getmro(meth.im_class):
    #        if meth.__name__ in cls.__dict__: return cls
    #    return None

    def do_opt_example(self, args):

        # FOR NOW DELETE THE COMMENTS THEY ARE FOR AN EVENTUAL DECORATOR
        #name = sys._getframe().f_code.co_name
        #help_name = name.replace("do_", "help_")
        # NOT YET SURE HOW TO GET MY OWN POINTER TO MY METHOD IA M IN
        #cls=  self._get_class(self.do_opt_example)
        #method = getattr(cls, help_name)
        #arguments = self._get_doc_args(method,args)
        
        arguments = self._get_doc_args(self.help_opt_example,args)
        print(arguments)
