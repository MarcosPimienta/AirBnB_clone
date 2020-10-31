#!/usr/bin/python3
""" Contains the entry point of the command interpreter """

import cmd
import models
from models.base_model import BaseModel

d = {"BaseModel": BaseModel}


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

        def do_show(self, arg):
                """Prints the string representation of an instance
                based on the class name and id"""
                args = arg.split()

                if len(args) == 0:
                        print("** class name missing **")
                        return False
                if args[0] not in d:
                        print("** class doesn't exist **")
                        return False
                if len(args) < 2:
                        print("** instance id missing **")
                        return False
                else:
                        s = "{}.{}".format(args[0], args[1])
                        if s not in models.storage.all():
                                print("** no instance found **")
                                return False
                        else:
                                print(models.storage.all()[s])

        def do_destroy(self, arg):
                """ Deletes an instance based on the class name and id """
                args = arg.split()

                if len(args) == 0:
                        print("** class name missing **")
                        return False
                if args[0] not in d:
                        print("** class doesn't exist **")
                        return False
                if len(args) < 2:
                        print("** instance id missing **")
                        return False
                else:
                        sk = "{}.{}".format(args[0], args[1])
                        if sk not in models.storage.all():
                                print("** no instance found **")
                                return False
                        else:
                                models.storage.all().pop(sk)
                                models.storage.save()

if __name__ == '__main__':
        HBNBCommand().cmdloop()
