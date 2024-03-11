#!/usr/bin/python3
"""Contains entry point of the command interpreter"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """HBNB console implementation"""
    prompt = "(hbnb) "

    def do_quit(self, line):
        return True

    def help_quit(self):
        print("Quit command to exit the program\n")

    def do_EOF(self, line):
        """Handles end-of-line character, exits program if encountered"""
        return True

    def do_create(self, line):
        if line == "":
            print("** class name missing **")
        elif line != "BaseModel":
            print("** class doesn't exist **")
        else:
            obj = BaseModel()
            obj.save()
            print(obj.id)

    def help_create(self):
        print("Creates a new instance of BaseModel, saves it and prints its id")
        print("Usage")
        print("=====")
        print("create [BaseModel]")

    def do_show(self, line):
        argList = line.split(' ')
        if argList[0] == '':
            print("** class name missing **")
        elif len(argList) == 1 and argList[0] != "BaseModel":
            print("**class doesn't exist **")
        elif len(argList) == 1 and argList[0] == "BaseModel":
            print("** instance id missing **")
        else:
            key = "{}.{}".format(argList[0], argList[1])
            obj = storage.all().get(key)
            if obj is None:
                print("** no instance found **")
            elif argList[0] in obj.values():
                obj = BaseModel(**obj)
                print(obj)

    def help_show(self):
        print("Prints the string representation of an instance based on class name and id")
        print("Usage")
        print("=====")
        print("show [BaseModel] [id]")
    
    def do_destroy(self, line):
        argList = line.split(' ')
        if argList[0] == '':
            print("** class name missing **")
        elif len(argList) == 1 and argList[0] != "BaseModel":
            print("**class doesn't exist **")
        elif len(argList) == 1 and argList[0] == "BaseModel":
            print("** instance id missing **")
        else:
            key = "{}.{}".format(argList[0], argList[1])
            obj = storage.all().get(key)
            if obj is None:
                print("** no instance found **")
            elif argList[0] in obj.values():
                del storage.all()[key]
                storage.save()

    def help_destroy(self):
        print("Deletes an instance based on class name and id")
        print("Usage")
        print("=====")
        print("destroy [BaseModel] [id]")

    def do_all(self, line):
        argList = line.split(' ')
        objs = storage.all()
        myList = [value for value in objs.values()]
        if len(argList) == 1 and argList[0] == "":
            print(storage.all())
        elif len(argList) == 1 and argList[0] != "BaseModel":
            print("**class doesn't exist **")
        elif len(argList) == 1 and argList[0] == "BaseModel": 
            print(storage.all())


if __name__ == "__main__":
    HBNBCommand().cmdloop("**Welcome to this console. Enter help or ? to get started.**\n\n")