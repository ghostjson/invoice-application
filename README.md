## Invoice Application

This is a desktop application to create and export invoices to excel sheets.


## Tech Stack
### Langauges
- python
- HTML,CSS
- Javascript
- bash

### Frameworks & Libraries	
- vuejs (v2)
- python eel
- python openpyxl
- materialize css
- jquery
- datatables

### database
- sqlite

## Run this project

To build this project,
- first create a python environment (recommended)

- install python dependencies using provided requirements.txt

- run `python3 invoice.py`

## Build

You can simply build this project by running `build.sh` file on root directory. Assuming you already install python3 on your system.

## Application Structure

### resources/
Contains template of invoice.

(Warning :warning: : Do not edit this unless you know what you are doing)

### ui/
Contains all html files which is responsible for how the UI of the application looks.

### database.db
It is a sqlite database used in the application.

### database.py
It is python script related to accessing database.

### invoice.py
Application entry point

### export.py
It is a python script related to exporting data to an excel sheet.