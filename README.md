# Authnet

Authnet is a project aimed to automate the wifi login process for an institution or a workplace.

### Installation

Authnet requires the webbot library for Python.
```sh
$ pip3 install webbot
```

### Setup

Go to the auth.py file and make changes in the following variables.
- period
- login_url
- username
- password
- username_element_id
- password_element_id

### Working

It takes the id of the html tag for the input fields.
Get the id by viewing the source of your page.
It uses that id to automatically input the username and password set by you.

### Todos

- make it more convenient (to be figured out how)
