#!/usr/bin/python3
"""A class HBNBcommand that contains the entry point of the
command interpreter"""
import cmd
import models
import shlex
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

classes = {"City": City, "Amenity": Amenity, "BaseModel": BaseModel,
           "State": State, "Place": Place, "Review": Review, "User": User}


class HBNBcommand(cmd.Cmd):
    """Module of a console"""
    prompt = "(hbnb)"

    def do_quit(self, args):
        return True

    def help_quit(self):
        print("exit the application")

    do_EOF = do_quit
    help_EOF = help_quit

    def emptyline(self):
        """ Causes an empty line + ENTER to not execute anything"""
        pass

    def do_create(self, args):
        """Creates a new instance of BaseModel, saves it (to the
         JSON file) and prints the id."""
        str_list = shlex.split(args)
        if len(str_list) == 0:
            print(" class name missing ")
            return
        if str_list[0] in classes:
            new_inst = eval(str_list[0])()
            new_inst.save()
            print(new_inst.id)
        else:
            print(" class doesn't exist ")

    def do_show(self, args):
        """ Prints the string representation of an instance based on the
         class name and id."""
        str_list = shlex.split(args)
        if len(str_list) == 0:
            print(" class name missing ")
            return
        elif str_list[0] not in classes:
            print(" class doesn't exist ")
        elif len(str_list) == 1:
            print(" instance id missing ")
        else:
            key = "{}.{}".format(str_list[0], str_list[1])
            if key in models.storage.all():
                print(models.storage.all()[key])
            else:
                print(" no instance found ")

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id (save the
         change into the JSON file). """
        str_list = shlex.split(args)
        if len(str_list) == 0:
            print(" class name missing ")
            return
        elif str_list[0] not in classes:
            print(" class doesn't exist ")
        elif len(str_list) == 1:
            print(" instance id missing ")
        else:
            key = "{}.{}".format(str_list[0], str_list[1])
            if key in models.storage.all():
                del models.storage.all()[key]
                models.storage.save()
            else:
                print(" no instance found ")

    def do_all(self, args):
        """Prints all string representation of all instances based or not
         on the class name."""
        str_list = shlex.split(args)
        my_list = []
        if len(str_list) == 0:
            for value in models.storage.all().values():
                my_list.append(str(value))
        elif str_list[0] in classes:
            for key in models.storage.all():
                if str_list[0] in key:
                    my_list.append(str(models.storage.all()[key]))
        else:
            print(" class doesn't exist ")
            return
        print(my_list)

    def do_update(self, args):
        """Updates an instance based on the class name and id by adding or
         updating attribute (save the change into the JSON file)."""
        st = models.storage.all()
        str_list = shlex.split(args)
        if len(str_list) == 0:
            print(" class name missing ")
        elif str_list[0] not in classes:
            print(" class doesn't exist ")
        elif len(str_list) < 2:
            print(" instance id missing ")
        else:
            key = "{}.{}".format(str_list[0], str_list[1])
            if key in st:
                if len(str_list) < 3:
                    print(" attribute name missing ")
                elif len(str_list) < 4:
                    print(" value missing ")
                else:
                    try:
                        st[key].dict[str_list[2]] = eval(str_list[3])
                    except(Exception):
                        st[key].dict[str_list[2]] = str_list[3]
                        st[key].save()
            else:
                print(" no instance found ")

    def count(self, args):
        """Retrieves the number of instances of a class"""
        str_list = shlex.split(args)
        counter = 0
        if str_list[0] not in classes:
            print(" class doesn't exist ")
            return
        else:
            objects = models.storage.all()
            for key in objects:
                name = key.split('.')
                if name[0] == str_list[0]:
                    counter += 1
            print(counter)

    def strip_args(self, args):
        """Strips the argument and returns a string of command"""
        my_list = []
        my_list.append(args[0])
        try:
            my_dict = eval(
                args[1][args[1].find('{'):args[1].find('}')+1])
        except (Exception):
            my_dict = None
        if isinstance(my_dict, dict):
            my_str = args[1][args[1].find('(')+1:args[1].find(')')]
            my_list.append(((my_str.split(", "))[0]).strip('"'))
            my_list.append(my_dict)
            return my_list
        my_str = args[1][args[1].find('(')+1:args[1].find(')')]
        my_list.append(" ".join(my_str.split(", ")))
        return " ".join(i for i in my_list)

    def default(self, args):
        """Handles custom format commands"""
        my_list = args.split('.')
        if len(my_list) >= 2:
            if my_list[1] == "all()":
                self.do_all(my_list[0])
            elif my_list[1] == "count()":
                self.count(my_list[0])
            elif my_list[1][:4] == "show":
                self.do_show(self.strip_args(my_list))
            elif my_list[1][:7] == "destroy":
                self.do_destroy(self.strip_args(my_list))
            elif my_list[1][:6] == "update":
                str_list = self.strip_args(my_list)
                if isinstance(str_list, list):
                    objects = models.storage.all()
                    key = "{}.{}".format(str_list[0], args[1])
                    for k, v in str_list[2].items():
                        self.do_update(key + ' "{}" "{}"'.format(k, v))
                else:
                    self.do_update(str_list)
        else:
            cmd.Cmd.default(self, args)


if name == 'main':
    HBNBcommand().cmdloop()
