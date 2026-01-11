#!/usr/bin/python3
"""
Console module
Command interpreter for AirBnB clone project
"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter class

    Attributes:
        prompt (str): The command prompt
        valid_classes (list): List of valid class names
    """
    prompt = "(hbnb) "
    valid_classes = [
        "BaseModel",
        "User",
        "State",
        "City",
        "Amenity",
        "Place",
        "Review"
    ]

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()
        return True

    def emptyline(self):
        """Do nothing when empty line is entered"""
        pass

    def do_create(self, arg):
        """
        Create a new instance of a class
        Usage: create <class_name>
        """
        if not arg:
            print("** class name missing **")
            return

        if arg not in self.valid_classes:
            print("** class doesn't exist **")
            return

        # Map class names to actual classes
        class_map = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
        }

        new_instance = class_map[arg]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """
        Print string representation of an instance
        Usage: show <class_name> <id>
        """
        args = arg.split()

        if len(args) == 0:
            print("** class name missing **")
            return

        if args[0] not in self.valid_classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = f"{args[0]}.{args[1]}"
        objects = storage.all()

        if key not in objects:
            print("** no instance found **")
            return

        print(objects[key])

    def do_destroy(self, arg):
        """
        Delete an instance based on class name and id
        Usage: destroy <class_name> <id>
        """
        args = arg.split()

        if len(args) == 0:
            print("** class name missing **")
            return

        if args[0] not in self.valid_classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = f"{args[0]}.{args[1]}"
        objects = storage.all()

        if key not in objects:
            print("** no instance found **")
            return

        del objects[key]
        storage.save()

    def do_all(self, arg):
        """
        Print string representation of all instances
        Usage: all or all <class_name>
        """
        objects = storage.all()
        obj_list = []

        if not arg:
            # Print all objects
            for obj in objects.values():
                obj_list.append(str(obj))
        else:
            # Check if class exists
            if arg not in self.valid_classes:
                print("** class doesn't exist **")
                return

            # Print objects of specific class
            for key, obj in objects.items():
                if key.startswith(arg + "."):
                    obj_list.append(str(obj))

        print(obj_list)

    def do_update(self, arg):
        """
        Update an instance based on class name and id
        Usage: update <class_name> <id> <attribute_name> "<attribute_value>"
        """
        args = arg.split()

        if len(args) == 0:
            print("** class name missing **")
            return

        if args[0] not in self.valid_classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = f"{args[0]}.{args[1]}"
        objects = storage.all()

        if key not in objects:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        obj = objects[key]
        attr_name = args[2]
        attr_value = args[3]

        # Remove quotes if present
        if attr_value.startswith('"') and attr_value.endswith('"'):
            attr_value = attr_value[1:-1]

        # Try to cast to appropriate type
        if hasattr(obj, attr_name):
            attr_type = type(getattr(obj, attr_name))
            try:
                attr_value = attr_type(attr_value)
            except (ValueError, TypeError):
                pass
        else:
            try:
                # Try int
                attr_value = int(attr_value)
            except ValueError:
                try:
                    # Try float
                    attr_value = float(attr_value)
                except ValueError:
                    # Keep as string
                    pass

        setattr(obj, attr_name, attr_value)
        obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
