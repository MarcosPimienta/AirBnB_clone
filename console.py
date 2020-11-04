#!/usr/bin/python3
""" Contains the entry point of the command interpreter """

import cmd
import models
import shlex
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.place import Place
from models.amenity import Amenity
from models.review import Review


d = {"BaseModel": BaseModel, "User": User, "City": City,
     "State": State, "Amenity": Amenity, "Place": Place, "Review": Review}


class HBNBCommand(cmd.Cmd):
        """ command interpreter """

        prompt = '(hbnb) '

        def do_quit(self, arg):
                """Quit command to exit the program
                """
                return True

        def do_EOF(self, arg):
                """Exit the program"""
                return True

        def emptyline(self):
                """prints prompt again"""
                pass

        def precmd(self, line):
                """Check for special cases in line command"""
                if line:
                        if line.isspace():
                                return line
                        ls = shlex.split(line)
                        if "." not in ls[0]:
                                return line
                        x = line.split(".", 1)
                        x1 = x[1].replace(")", "")
                        x1 = x1.split("(")
                        x2 = []
                        x2.append(x1[0])
                        x2.append(x[0])
                        if len(x1[1]) > 0:
                                x3 = x1[1].split(", ")
                                lenx3 = len(x3)
                                for i in range(len(x3)):
                                        x2.append(x3[i])
                        command_line = " ".join(x2)
                        return command_line
                else:
                        return line

        def do_create(self, arg):
                """Creates a new instance of BaseModel,
                saves it (to the JSON file) and prints the id"""
                args = shlex.split(arg)

                if len(args) == 0:
                        print("** class name missing **")
                        return False
                if args[0] not in d:
                        print("** class doesn't exist **")
                        return False
                ins = d[args[0]]()
                ins.save()
                print(ins.id)

        def do_show(self, arg):
                """Prints the string representation of an instance
                based on the class name and id"""
                args = shlex.split(arg)

                if len(args) == 0:
                        print("** class name missing **")
                        return False
                if args[0] not in d:
                        print("** class doesn't exist **")
                        return False
                if len(args) < 2:
                        print("** instance id missing **")
                        return False
                s = "{}.{}".format(args[0], args[1])
                if s not in models.storage.all():
                        print("** no instance found **")
                        return False
                print(models.storage.all()[s])

        def do_destroy(self, arg):
                """ Deletes an instance based on the class name and id """
                args = shlex.split(arg)

                if len(args) == 0:
                        print("** class name missing **")
                        return False
                if args[0] not in d:
                        print("** class doesn't exist **")
                        return False
                if len(args) < 2:
                        print("** instance id missing **")
                        return False
                sk = "{}.{}".format(args[0], args[1])
                if sk not in models.storage.all():
                        print("** no instance found **")
                        return False
                models.storage.all().pop(sk)
                models.storage.save()

        def do_all(self, arg):
                """Prints all string representation of all instances based or
                not on the class name"""
                args = shlex.split(arg)
                lt = []
                if len(args) == 0:
                        for val in models.storage.all().values():
                                lt.append(str(val))
                        print(lt)
                else:
                        if args[0] not in d:
                                print("** class doesn't exist **")
                        else:
                                for val in models.storage.all().values():
                                        if type(val).__name__ == args[0]:
                                                lt.append(str(val))
                                print(lt)

        def do_update(self, arg):
                """Updates an instance based on the class name and id by
                adding or updating attribute"""
                args = shlex.split(arg)
                if len(args) == 0:
                        print("** class name missing **")
                        return False
                if args[0] not in d:
                        print("** class doesn't exist **")
                        return False
                if len(args) < 2:
                        print("** instance id missing **")
                        return False
                key = "{}.{}".format(args[0], args[1])
                if key not in models.storage.all():
                        print("** no instance found **")
                        return False
                if len(args) < 3:
                        print("** attribute name missing **")
                        return False
                if len(args) < 4:
                        print("** value missing **")
                        return False
                if args[3].isdecimal():
                        args[3] = int(args[3])
                else:
                        try:
                                args[3] = float(args[3])
                        except:
                                pass
                setattr(models.storage.all()[key], args[2], args[3])
                models.storage.save()

        def do_count(self, arg):
                """Retrieve the number of instances of a class"""

                args = shlex.split(arg)
                cter = 0

                if len(args) == 0:
                        print("** class name missing **")
                        return False

                for val in models.storage.all().values():
                        if val.__class__.__name__ == args[0]:
                                cter += 1
                print(cter)

if __name__ == '__main__':
        HBNBCommand().cmdloop()
