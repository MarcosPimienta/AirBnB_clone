#!/usr/bin/python3
""" Contains the entry point of the command interpreter """

import cmd
import models
from models.base_model import BaseModel


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

        def do_create(self, arg):
                """Creates a new instance of BaseModel,
                saves it (to the JSON file) and prints the id"""
                args = arg.split()
                d = {"BaseModel": BaseModel}
                if len(args) == 0:
                        print("** class name missing **")
                        return False
                if args[0] not in d:
                        print("** class doesn't exist **")
                        return False
                else:
                        ins = d[args[0]]()
                        ins.save()
                        print(ins.id)

if __name__ == '__main__':
        HBNBCommand().cmdloop()
