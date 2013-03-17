#! /usr/bin/env python
import cmd
import string
import sys
import os
import glob
import textwrap

imports = []
add_bases = ()

def importer(regex):
    global imports
    plugins = glob.glob(regex)
    if plugins:
        for filename in plugins:
            filename = filename.replace(".py", "")
            (dir, plugin) = filename.split("/")
            importer_line =  "from %(dir)s.%(plugin)s import %(plugin)s as %(plugin)s" % {"plugin": plugin, "dir": dir}
            imports.append(importer_line)
            print "Loading Plugin:", plugin

importer("plugins/shell_*.py")

for import_line in imports:
    # I am just doing exec and not __import__ for now due to simplicity
    exec(import_line)


#
# no dynamic loading yet
#


class Shell(cmd.Cmd,
            shell_opt_example,
            shell_util,
            shell_banner,
            shell_scope):
            

    scopes = ['rain', 'gregor']

    ######################################################################
    # DO NOT CAHNGE
    ######################################################################

    preloop = shell_banner.preloop
    prompt  = shell_scope.prompt
    precmd  = shell_scope.precmd
    emptyline = shell_scope.emptyline
    
    ######################################################################
    # Info Command
    ######################################################################
    def help_info(self):
        msg = """
        DESCRIPTION

           provides information that is maintained internally in the shell
            
        """
        print textwrap.dedent(msg)

        
    def do_info(self,arg):
        print "%20s =" % "Scripts", str(self.scripts)
        print "%20s =" % "Variables", str(self.variables)
        print "%20s =" % "Echo", str(self.echo)
        print "%20s =" % "Scope", self.scope
        print "%20s =" % "With scope", self.scopes
        print "%20s =" % "No scope", self.scopeless



    ######################################################################
    # Sample Command
    ######################################################################

    def do_gregor(self,arg):
        print "GREGOR", arg

    def do_rain(self,arg):
        print "RAIN ", arg



if __name__ == "__main__":
    shell = Shell()
    shell.cmdloop()
