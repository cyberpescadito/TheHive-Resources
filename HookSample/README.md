# HookSample

The purpose of this sample is to provide example of webhook creation & syntax.

In this sample, when a case with the customfield "TLA" is updated, it will look in libraries to check to which region belong the city (eg: PAR belong to region EU), and automatically send an update of the case with Region customfield fulfilled in TheHive.

Feel free to adapt and modify it according to your needs.

# How to use it

Place the handlers.py in your folder thehive_hooks

Change the content of the api variable in handlers.py according to your context

Run the flask

# Dependences :

Python

TheHive4py library

json library

TheHiveHooks, you can install it following (https://github.com/TheHive-Project/TheHiveHooks)

# Author
* [Florian Perret](https://twitter.com/cyber_pescadito)
* license : **AGPL V3**

