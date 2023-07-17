#!/usr/bin/python3
"""console module that contains entry point command interpreter"""

import cmd


class HBNBCommand(cmd.Cmd):
    """Command Interpreter class"""

    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit command do exit the program"""
        return True

    def do_EOF(self, line):
        """Handles End Of File command"""
        print()
        return True

    def emptyline(self):
        """do nothing when ENTER is entered"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()

