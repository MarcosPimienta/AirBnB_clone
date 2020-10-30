#!/usr/bin/python3
""" Contains the entry point of the command interpreter """

import cmd


class HBNBCommand(cmd.Cmd):
        """ command interpreter """

        prompt = '(hbnb) '

        def do_quit(self, arg):
                """Quit command to exit the program"""
                return True

        def do_EOF(self, arg):
                """Exit the program"""
                return True

        def emptyline(self):
                """prints prompt again"""
                pass

if __name__ == '__main__':
        HBNBCommand().cmdloop()
