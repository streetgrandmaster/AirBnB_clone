#!/usr/bin/python3
"""A class HBNBCommand that contains the entry point of the
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


class HBNBCommand(cmd.Cmd):
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
            print("** class name missing **")
            return
        if str_list[0] in classes:
            new_inst = eval(str_list[0])()
            new_inst.save()
            print(new_inst.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, args):
        """ Prints the string representation of an instance based on the
         class name and id."""
        str_list = shlex.split(args)
        if len(str_list) == 0:
            print("** class name missing **")
            return
        if str_list[0] not in classes:
            print("** class doesn't exist **")
        if len(str_list) == 1:
            print("** instance id missing **")
        elif len(str_list) > 1:
            key = "{}.{}".format(str_list[0], str_list[1])
            if key in models.storage.all():
                print(models.storage.all()[key])
            else:
                print("** no instance found **")

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id (save the
         change into the JSON file). """
        str_list = shlex.split(args)
        if len(str_list) == 0:
            print("** class name missing **")
            return
        if str_list[0] not in classes:
            print("** class doesn't exist **")
        if len(str_list) == 1:
            print("** instance id missing **")
        elif len(str_list) > 1:
            key = "{}.{}".format(str_list[0], str_list[1])
            if key in models.storage.all():
                del models.storage.all()[key]
                models.storage.save()
            else:
                print("** no instance found **")

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
            print("** class doesn't exist **")
            return
        print(my_list)

    def do_update(self, args):
        """Updates an instance based on the class name and id by adding or
         updating attribute (save the change into the JSON file)."""
        str_list = shlex.split(args)
        if len(str_list) == 0:
            print("** class name missing **")
            return
        if str_list[0] not in classes:
            print("** class doesn't exist **")
        if len(str_list) == 1:
            print("** instance id missing **")
            return
        key = "{}.{}".format(str_list[0], str_list[1])
        if key in models.storage.all():
            print(models.storage.all()[key])
        else:
            print("** no instance found **")
            return
        if (len(str_list) == 2):
            print("** attribute name missing **")
            return
        if (len(str_list) == 3):
            print("** value missing **")
            return
        setattr(models.storage.all()[key], str_list[2], str_list[3])
        models.storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
