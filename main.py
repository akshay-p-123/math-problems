import gui
 
cred = open('user_pass.txt','r')

#initializes window
#contorller takes a parameter of a text file in 'read' mode
log_in = gui.Controller(cred)
log_in.mainloop()

