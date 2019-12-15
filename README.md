# Codeforces Scrapper
A script to get user data from Codeforces

## Usage
The script can be run with the following arguments:

#### `--handle [user handle]`
Directly enter the handle of the user whose data you want to get.

#### `--no-gui`
Print user data to terminal instead of creating a GUI to show them.

#### `--help`
Show this help.

## To build .deb
#### First make sure the modules in `requirements.txt` are installed on your system!
Run `python setup.py --command-packages=stdeb.command bdist_deb`

The .deb will then be available in `deb_list/` directory.
