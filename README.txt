run this in the terminal: python app.py

then a cool website with several ok buttons will be loaded

acording to you creativity, here are examples of things the OK button can do: 
 1 copy commands to be pasted in some terminal or script
 2 send commands to execution
 3 send tcl script to execution by vmd, ( but that only works if the vmd has been oppended with a socket)


to add a new ok button you do this:

1-create a function on myfuncions.py
2-define the page structure in config.json

in each expandable box, be sure to put in the key inputbox (with some number so that the key is unique) or radiobutton (with a number too) or ok_button
in the "ok_button" key, you should put the function to be called whe the OK button is clicked. 
the arguments will be everithing set in the imput boxes of that section. 
be sure to set the arguments properly in the function definition so to match what will be sent



