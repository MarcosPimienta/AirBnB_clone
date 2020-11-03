# AirBnB clone project ![Diagram](https://github.com/MarcosPimienta/holbertonschool-higher_level_programming/blob/master/img/AirBnbDiagram.png)

This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

## Table of Contents

    Authors
    How To Installation
    How To Use
    Some Commands
    Examples

### Authors

    Ana Ruth Morales - Ana-Morales <1776@holbertonschool.com>
    Marcos Pimienta - MarcosPimienta <1676@holbertonschool.com>

## Installation

To use the command line interpreter it is necessary to install it by using the following commands from your terminal:

    git clone https://github.com/Ana-Morales/AirBnB_clone.git

This will create a new directory named "AirBnB_clone", now move to the directory using:

    AirBnB_clone/

Now you will be inside the AirBnB_clone directory and you will see different files. These files are python modules or folders that contain other modules.

Congrats, now you have our cmd line interpreter running in your machine.

## Use

In order to execute this cmd line interpreter just type from your terminal the command

    ./console.py

It will open a prompt and it will look like this

    (hbnb) 

You are on the cmd line interpreter and it is waiting for you to type and execute a command. Next you will see a list of commands. it will show you how you can exit the shell.
    
Or you can also do Ctrl + D And this will also terminate the simple shell.

### Some Commands

Here is a list of some commands you can use, there are many more, try to experiment with it.
    
    (hbnb) EOF
    (hbnb) all
    (hbnb) count
    (hbnb) create
    (hbnb) destroy
    (hbnb) help
    (hbnb) quit
    (hbnb) show
    (hbnb) update

### Examples of use

*Let's take a look at these examples:*

    (hbnb) create <class name>
    (hbnb) update <class name>
    (hbnb) destroy <class name>
create will create an instance based from the parent class "BaseModel" and then it will store it on a .json file
update will update an instance based from the <class name> and then it will remove the previous .json file and store it on a new .json file
destroy will remove the instance based from the <class name> and then it will remove the previous .json file and store it on a new .json file
