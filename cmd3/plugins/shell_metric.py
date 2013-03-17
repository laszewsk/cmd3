"""
@options([
        make_option('-f', '--start_date', type="string", help="start time of the interval (type. 
        make_option('-t', '--end_date', type="string", help="end time of the interval (type. YYYY-MM-DDThh:mm:ss)"),
        make_option('-M', '--month', type="int", help="month to analyze (type. MM)"),
        make_option('-Y', '--year', type="int", help="year to analyze (type. YYYY)"),
        make_option('-m', '--metric', dest="metric", type="string", help="item name to measure (e.g. runtime, count)"),
        make_option('-P', '--period', dest="period", type="string", help="search period (monthly, daily)")
        ])
"""

import textwrap
from docopt import docopt
import inspect
import sys
import importlib
from  util.decorators import help_method
from  util.decorators import _get_doc_args

class shell_metric:

    ######################################################################
    # analyze commands
    ######################################################################

    @help_method
    def help_analyze(self):
        """
        Usage:
               analyze METRIC --start START --end END 
               analyze METRIC --period [monthly|quaterly|daily]
               analyze METRIC --month MONTH

        Analyze the metric data

        Arguments:
            METRIC     The metric to be analyzed ... what values does it havet ...
            START      The start time n the format YYYY-MM-DDThh:mm:ss
            ENDT       The end time n the format YYYY-MM-DDThh:mm:ss
            MONTH      The month in 01,02, ..., 12

        Options:
          --start     specifies the time when to start the analysis
          --end       specified the time when to end the analysis
          --month     the month
          --period    the period

        """

    def do_analyze(self, args):
        arguments = _get_doc_args(self.help_analyze,args)
        print(arguments)

    ######################################################################
    # CVS commands
    ######################################################################
    @help_method
    def help_table(self):
        """
        Usage:
               table FILENAME
               table --file FILENAME

        Export the data in cvs format to a file. Former cvs command

        Arguments:
            FILENAME   The filename

        Options:
          --filet     specifies the filename

        """
	
    def do_table(self, args):
        arguments = _get_doc_args(self.help_table,args)
        print(arguments)
