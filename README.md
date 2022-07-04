<h1 style="color: #006cff; font-size: 50px;"><img style="margin-bottom: -15px;" src="doc_files/logoSolid.png" width="70"/> SOFT DEVELOPMENT </h1>

# WHL FILE EXAMPLE
This project contains an example of building a platform agnostic whl file
that produces both modules that can be imported or run in terminal.

## Example includes:
* Specify CLI commands to run on console
* Packaging resource files (text, images, etc)
* Accessing packaged resource files

## Building whl file:
Contained are a series of shell scripts to run. For systems that don't
support shell scripts, the contained command can be run in cosole as-is.

* buildWhl.sh: build whl file which can be found in the generated dist folder.
* installWhlTools.sh: installs needed python modules for building whl files.