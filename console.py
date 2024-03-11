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
        myList = []
        if len(argList) == 1 and (argList[0] == "" or argList[0] == "BaseModel"):
            for key, value in objs.items():
                obj = BaseModel(**value)
                myList.append(str(obj))
            print(myList)
        elif len(argList) == 1 and argList[0] != "BaseModel":
            print("** class doesn't exist **")

    def help_all(self):
        print("Prints all string representation of all instances based on class name or not")
        print("Usage")
        print("=====")
        print("all or all [BaseModel]")

    def do_update(self, line):
        argList = line.split(' ')
        if len(argList) == 1 and argList[0] == "":
            print("** class name missing **")
        elif len(argList) == 1 and argList[0] != "BaseModel":
            print("**class doesn't exist **")
        elif len(argList) == 1 and argList[0] == "BaseModel":
            print("** instance id missing **")
        else:
            key = "{}.{}".format(argList[0], argList[1])
            if key in storage.all():
                if len(argList) == 2 and argList[0] == "BaseModel":
                    print("** attribute name missing **")
                elif len(argList) == 3 and argList[0] == "BaseModel":
                    print("** value missing **")
                else:
                    storage.all()[key][argList[2]] = argList[3].strip('"')
                    storage.save()
            else:
                print("** no instance found **")
    
    def help_update(self):
        print("Updates an instance based on the class name and id by adding or updating attribute")
        print("Usage")
        print("=====")
        print("update <class name> <id> <attribute name> \"<attribute value>\"")

if __name__ == "__main__":
    HBNBCommand().cmdloop("**Welcome to this console. Enter help or ? to get started.**\n\n")
