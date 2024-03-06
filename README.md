# AirBnB_clone

## Description

The goal of this project is to deploy on my server a simple copy of the AirBnB website.

This project won't be built all at once, but step by step.

Here are the steps:

### Steps

#### The console

With the console you can:
* create your data model
* manage(create, update, destroy,etc)
* store and persist objects to a file(JSON file)

The first piece is to manage a powerful storage system. This storage engine will give us an abstraction between "My object" and "How they are stored and persisted". This means from the console code(the command interpreter itself) and from the front-end and RestAPI i will build later, i wouldn't have to pay attention of how my objects are stored.

This abstraction allows for changing the type of storage easily without having to update all of my codebase.

The console will be a tool to validate this storage engine.
