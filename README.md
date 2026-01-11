# AirBnB Clone – The Console Made by Mufaro Victoria Kunze and Esther Kirabo

This project is the first step towards building a full web application: an AirBnB clone.  
In this stage, we implement a **command-line interpreter (console)** that allows us to manage AirBnB objects.

The console is responsible for:
- Creating new objects (Users, Places, etc.)
- Retrieving objects from storage
- Updating object attributes
- Deleting objects
- Persisting data using JSON serialization

This console forms the foundation for later stages, including a web interface, database storage, and RESTful APIs.

---

## Command Interpreter Description

The command interpreter is a shell-like program that enables interaction with the application’s core objects.  
It works in **interactive mode** and **non-interactive mode**, similar to a UNIX shell.

---

## How to Start the Command Interpreter

### Interactive Mode

```bash
$ ./console.py
(hbnb)

### Non-Interactive Mode

$ echo "help" | ./console.py
(hbnb)
* Make sure the file is executable (chmod +x console.py)

Repository and File Structure
.
├── AUTHORS
├── README.md
├── console.py
├── models/
│   ├── __init__.py
│   ├── base_model.py
│   ├── user.py
│   ├── state.py
│   ├── city.py
│   ├── amenity.py
│   ├── place.py
│   ├── review.py
│   └── engine/
│       ├── __init__.py
│       └── file_storage.py
└── tests/
    ├── __init__.py
    └── test_models/

Authors

See the AUTHORS file for a full list of contributors.