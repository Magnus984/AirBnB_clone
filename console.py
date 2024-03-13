#!/usr/bin/python3
"""Contains entry point of the command interpreter"""
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


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
        classList = [
                'BaseModel', 'User',
                'State', 'City', 'Amenity', 'Place', 'Review'
                ]
        if line == "":
            print("** class name missing **")
        elif line not in classList:
            print("** class doesn't exist **")
        else:
            if line == "BaseModel":
                obj = BaseModel()
                obj.save()
                print(obj.id)
            elif line == "User":
                obj = User()
                obj.save()
                print(obj.id)
            elif line == "State":
                obj = State()
                obj.save()
                print(obj.id)
            elif line == "City":
                obj = City()
                obj.save()
                print(obj.id)
            elif line == "Amenity":
                obj = Amenity()
                obj.save()
                print(obj.id)
            elif line == "Place":
                obj = Place()
                obj.save()
                print(obj.id)
            elif line == "Review":
                obj = Review()
                obj.save()
                print(obj.id)

    def help_create(self):
        print("Creates a new instance of class, saves it and prints its id")
        print("Usage")
        print("=====")
        print("create [class]")

    def do_show(self, line):
        argList = line.split(' ')
        classList = [
                'BaseModel', 'User', 'State',
                'City', 'Amenity', 'Place', 'Review'
                ]
        if argList[0] == '':
            print("** class name missing **")
        elif len(argList) == 1 and argList[0] not in classList:
            print("**class doesn't exist **")
        elif len(argList) == 1 and argList[0] in classList:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(argList[0], argList[1])
            obj = storage.all().get(key)
            if obj is None:
                print("** no instance found **")
            elif argList[0] in obj.values():
                if argList[0] == classList[0]:
                    obj = BaseModel(**obj)
                    print(obj)
                elif argList[0] == classList[1]:
                    obj = User(**obj)
                    print(obj)
                elif argList[0] == classList[2]:
                    obj = State(**obj)
                    print(obj)
                elif argList[0] == classList[3]:
                    obj = City(**obj)
                    print(obj)
                elif argList[0] == classList[4]:
                    obj = Amenity(**obj)
                    print(obj)
                elif argList[0] == classList[5]:
                    obj = Place(**obj)
                    print(obj)
                elif argList[0] == classList[6]:
                    obj = Review(**obj)
                    print(obj)

    def help_show(self):
        print("Prints the string representation of an instance")
        print("based on class name and id")
        print("Usage")
        print("=====")
        print("show [BaseModel] [id]")

    def do_destroy(self, line):
        argList = line.split(' ')
        classList = [
                'BaseModel', 'User', 'State',
                'City', 'Amenity', 'Place', 'Review'
                ]
        if argList[0] == '':
            print("** class name missing **")
        elif len(argList) == 1 and argList[0] not in classList:
            print("**class doesn't exist **")
        elif len(argList) == 1 and argList[0] in classList:
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
        print("destroy [class] [id]")

    def do_all(self, line):
        argList = line.split(' ')
        classList = [
                'BaseModel', 'User', 'State',
                'City', 'Amenity', 'Place', 'Review'
                ]
        objs = storage.all()
        myList = []
        if len(argList) == 1 and (argList[0] == "" or argList[0] in classList):
            for key, value in objs.items():
                if value["__class__"] == classList[0]:
                    obj = BaseModel(**value)
                    myList.append(str(obj))
                elif value["__class__"] == classList[1]:
                    obj = User(**value)
                    myList.append(str(obj))
                elif value["__class__"] == classList[2]:
                    obj = State(**value)
                    myList.append(str(obj))
                elif value["__class__"] == classList[3]:
                    obj = City(**value)
                    myList.append(str(obj))
                elif value["__class__"] == classList[4]:
                    obj = Amenity(**value)
                    myList.append(str(obj))
                elif value["__class__"] == classList[5]:
                    obj = Place(**value)
                    myList.append(str(obj))
                elif value["__class__"] == classList[6]:
                    obj = Review(**value)
                    myList.append(str(obj))
            print(myList)
        elif len(argList) == 1 and argList[0] not in classList:
            print("** class doesn't exist **")

    def help_all(self):
        print("Prints all string representation of all instances")
        print("based on class name or not")
        print("Usage")
        print("=====")
        print("all or all [class]")

    def do_update(self, line):
        argList = line.split(' ')
        classList = [
                'BaseModel', 'User', 'State',
                'City', 'Amenity', 'Place', 'Review'
                ]
        if len(argList) == 1 and argList[0] == "":
            print("** class name missing **")
        elif len(argList) == 1 and argList[0] not in classList:
            print("**class doesn't exist **")
        elif len(argList) == 1 and argList[0] in classList:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(argList[0], argList[1])
            if key in storage.all():
                if len(argList) == 2 and argList[0] in classList:
                    print("** attribute name missing **")
                elif len(argList) == 3 and argList[0] in classList:
                    print("** value missing **")
                else:
                    storage.all()[key][argList[2]] = argList[3].strip('"')
                    storage.save()
            else:
                print("** no instance found **")

    def help_update(self):
        print("Updates an instance based on the class name and id")
        print("by adding or updating attribute")
        print("Usage")
        print("=====")
        print("update class name id attribute name \"<attribute value>\"")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
