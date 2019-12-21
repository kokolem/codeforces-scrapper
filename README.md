<h1 align="center">Codeforces Scrapper</h1>

<div align="center">
  
  Script to get user data from Codeforces.
  
  ![GitHub](https://img.shields.io/github/license/kokolem/codeforces-scrapper)
  ![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/kokolem/codeforces-scrapper)
  ![GitHub last commit](https://img.shields.io/github/last-commit/kokolem/codeforces-scrapper)
  
</div>

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
