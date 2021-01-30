# sublime-java-builder

a simple java builder for sublime written in python, support only windows, can also be used directly in command line, currently support 2 options: autorun for automaticly run the application after a success compilation and autoclear for automaticly clear the console before running the application.
note: omit the java extension when passing the file_name argument.
note: your python interpreter need to have support to run python script without using the python command, but if you still need to pass the python command then you could try to modify the builder.py and increment all the argv indexes by 1 

usage:
build.py file_name_no_extension autorun autoclear

note: autorun and autoclear is optional

you can email me at: adithxd@gmail.com
