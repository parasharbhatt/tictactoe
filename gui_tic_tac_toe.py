import sys
from tkinter import Tk, Button, Radiobutton,Label, Frame, Menu ,StringVar,IntVar

root = Tk()

root.title('Tic Tac Toe 1.0')
root.geometry("350x375")

my_menu=Menu(root)
root.config(menu=my_menu)

global player1_choice , player2_choice, turn ,btn_text1,btn_text2,btn_text3,btn_text4,btn_text5,btn_text6,btn_text7,btn_text8,btn_text9
global checked, done ,player1_Select , player2_Select ,results, win
op=""
r = IntVar()
r.set(1)
btn_text1 = StringVar()
btn_text1.set("")
btn_text2 = StringVar()
btn_text2.set("")
btn_text3 = StringVar()
btn_text3.set("")
btn_text4 = StringVar()
btn_text4.set("")
btn_text5 = StringVar()
btn_text5.set("")
btn_text6 = StringVar()
btn_text6.set("")

btn_text7= StringVar()
btn_text7.set("")
btn_text8 = StringVar()
btn_text8.set("")
btn_text9 = StringVar()
btn_text9.set("")

checked=[0,0,0,0,0,0,0,0,0]
done = 0
win=""

player1_choice=""
player2_choice=""
player1_Select = []
player2_Select= []
results =[(1,2,3), (4,5,6) , (7,8,9) ,\
          (1,4,7), (2,5,8) , (3,6,9), \
          (1,5,9), (3,5,7)]
turn=""

def file_new():
	global player1_choice , player2_choice, turn ,btn_text1,btn_text2,btn_text3,btn_text4,btn_text5,btn_text6,btn_text7,btn_text8,btn_text9
	global checked, done ,player1_Select , player2_Select ,results, win
	op=""
	r = IntVar()
	r.set(1)
	btn_text1 = StringVar()
	btn_text1.set("")
	btn_text2 = StringVar()
	btn_text2.set("")
	btn_text3 = StringVar()
	btn_text3.set("")
	btn_text4 = StringVar()
	btn_text4.set("")
	btn_text5 = StringVar()
	btn_text5.set("")
	btn_text6 = StringVar()
	btn_text6.set("")
	btn_text7= StringVar()
	btn_text7.set("")
	btn_text8 = StringVar()
	btn_text8.set("")
	btn_text9 = StringVar()
	btn_text9.set("")
	checked=[0,0,0,0,0,0,0,0,0]
	done = 0
	win=""

	player1_choice=""
	player2_choice=""
	player1_Select = []
	player2_Select= []
	results =[(1,2,3), (4,5,6) , (7,8,9) ,\
          (1,4,7), (2,5,8) , (3,6,9), \
          (1,5,9), (3,5,7)]
	turn=""


	text="New Game: Player-1 Select your option:"
	op="NEW"
	pass_info(text,op)
	#print(text)
	
def quit_app():
	sys.exit()
def fn_dummy():
	pass	
def button_click(bt,fp,fs,ls,n):
	global player1_choice , player2_choice, turn ,btn_text1,btn_text2,btn_text3,btn_text4,btn_text5,btn_text6,btn_text7,btn_text8,btn_text9, checked, done
	global player1_Select , player2_Select ,results ,win
	#print(f"Inside button_click: n={n} currnet turn={turn} player1_choice={player1_choice}, player2_choice={player2_choice}")
	if win != "" or done >=9:
		return
		
	if turn=="Player-1" :
		player1_Select.append(n)
	elif turn=="Player-2" :
		player2_Select.append(n)
		
	if checked[n-1] != 1:
		checked[n-1]=1
		done += 1
		#print(f"done= {done}, checked={checked}")
		
	if n==1:
		
		if turn=="Player-1" :
			turn="Player-2"
			btn_text1=str(player1_choice)
		elif turn=="Player-2" :
			turn="Player-1"
			btn_text1=str(player2_choice)
		bt.grid_forget()
		button_1 = Button(fp, text=btn_text1 , width=13, height=4, padx=0, pady=0  , command=lambda: fn_dummy)
		button_1.grid(row=0,column=0)
		button_1["state"]="disabled"
		
	if n==2:
		if turn=="Player-1" :
			turn="Player-2"
			btn_text2=str(player1_choice)
		elif turn=="Player-2" :
			turn="Player-1"
			btn_text2=str(player2_choice)
		bt.grid_forget()
		button_2 = Button(fp, text=btn_text2 , width=13, height=4, padx=0, pady=0  , command=lambda: fn_dummy)
		button_2.grid(row=0,column=1)
		button_2["state"]="disabled"
	if n==3:
		if turn=="Player-1" :
			turn="Player-2"
			btn_text3=str(player1_choice)
		elif turn=="Player-2" :
			turn="Player-1"
			btn_text3=str(player2_choice)
		bt.grid_forget()
		button_3 = Button(fp, text=btn_text3 , width=13, height=4, padx=0, pady=0 , command=lambda: fn_dummy)
		button_3.grid(row=0,column=2)
		button_3["state"]="disabled"

	if n==4:
		if turn=="Player-1" :
			turn="Player-2"
			btn_text4=str(player1_choice)
		elif turn=="Player-2" :
			turn="Player-1"
			btn_text4=str(player2_choice)
		bt.grid_forget()
		button_4 = Button(fp, text=btn_text4 , width=13, height=4, padx=0, pady=0  , command=lambda: fn_dummy)
		button_4.grid(row=1,column=0)
		button_4["state"]="disabled"
		
	if n==5:
		if turn=="Player-1" :
			turn="Player-2"
			btn_text5=str(player1_choice)
		elif turn=="Player-2" :
			turn="Player-1"
			btn_text5=str(player2_choice)
		bt.grid_forget()
		button_5 = Button(fp, text=btn_text5 , width=13, height=4, padx=0, pady=0  , command=lambda: fn_dummy)
		button_5.grid(row=1,column=1)
		button_5["state"]="disabled"
	if n==6:
		if turn=="Player-1" :
			turn="Player-2"
			btn_text6=str(player1_choice)
		elif turn=="Player-2" :
			turn="Player-1"
			btn_text6=str(player2_choice)
		bt.grid_forget()
		button_6 = Button(fp, text=btn_text6  , width=13, height=4, padx=0, pady=0 , command=lambda: fn_dummy)
		button_6.grid(row=1,column=2)
		button_6["state"]="disabled"
	

	if n==7:
		if turn=="Player-1" :
			turn="Player-2"
			btn_text7=str(player1_choice)
		elif turn=="Player-2" :
			turn="Player-1"
			btn_text7=str(player2_choice)
		bt.grid_forget()
		button_7 = Button(fp, text=btn_text7 , width=13, height=4, padx=0, pady=0 , command=lambda: fn_dummy)
		button_7.grid(row=2,column=0)
		button_7["state"]="disabled"
		
	if n==8:
		if turn=="Player-1" :
			turn="Player-2"
			btn_text8=str(player1_choice)
		elif turn=="Player-2" :
			turn="Player-1"
			btn_text8=str(player2_choice)
		bt.grid_forget()
		button_8 = Button(fp, text=btn_text8 , width=13, height=4, padx=0, pady=0  , command=lambda: fn_dummy)
		button_8.grid(row=2,column=1)
		button_8["state"]="disabled"
		
	if n==9:
		if turn=="Player-1" :
			turn="Player-2"
			btn_text9=str(player1_choice)
		elif turn=="Player-2" :
			turn="Player-1"
			btn_text9=str(player2_choice)
		bt.grid_forget()
		button_9 = Button(fp, text=btn_text9 , width=13, height=4, padx=0, pady=0 , command=lambda: fn_dummy)
		button_9.grid(row=2,column=2)
		button_9["state"]="disabled"

	player1_Select.sort()
	player2_Select.sort()
	#print(f"player1_Select = {player1_Select}")
	#print(f"player2_Select = {player2_Select}")
	
	if done >= 5 and win=="":
		for r1,r2,r3 in results:
			if r1 in player1_Select and r2 in player1_Select and r3 in player1_Select:
				win="Player1-Wins"
			elif r1 in player2_Select and r2 in player2_Select and r3 in player2_Select:
				win="Player2-Wins"
			if win!="":
				break
		if win!="" or done==9:
			turn="Geme Over"
		if win=="" and done==9:
			turn="Geme Over, No Player Wins !!"
			
		
	
	ls.grid_forget()
	lbltext="Turn -->"+turn+" "+win
	ls = Label(fs,text= lbltext)
	ls.grid(row=0,column=0)
	
	
def game_start(fp,fs):
	# define button
	global player1_choice , player2_choice, turn
	lbl_status = Label(fs,text= "Turn -->"+turn)
	lbl_status.grid(row=0,column=1)
	button_1 = Button(fp, textvariable=btn_text1 , width=13, height=4, padx=0, pady=0 , command=lambda: button_click(button_1,fp,fs,lbl_status,1))
	button_2 = Button(fp, textvariable=btn_text2 , width=13, height=4, padx=0, pady=0 , command=lambda: button_click(button_2,fp,fs,lbl_status,2))
	button_3 = Button(fp, textvariable=btn_text3 , width=13, height=4, padx=0, pady=0 , command=lambda: button_click(button_3,fp,fs,lbl_status,3))
	button_4 = Button(fp, textvariable=btn_text4 , width=13, height=4, padx=0, pady=0 , command=lambda: button_click(button_4,fp,fs,lbl_status,4))
	button_5 = Button(fp, textvariable=btn_text5 , width=13, height=4, padx=0, pady=0 , command=lambda: button_click(button_5,fp,fs,lbl_status,5))
	button_6 = Button(fp, textvariable=btn_text6 , width=13, height=4, padx=0, pady=0 , command=lambda: button_click(button_6,fp,fs,lbl_status,6))
	button_7 = Button(fp, textvariable=btn_text7 , width=13, height=4, padx=0, pady=0 , command=lambda: button_click(button_7,fp,fs,lbl_status,7))
	button_8 = Button(fp, textvariable=btn_text8 , width=13, height=4, padx=0, pady=0 , command=lambda: button_click(button_8,fp,fs,lbl_status,8))
	button_9 = Button(fp, textvariable=btn_text9 , width=13, height=4, padx=0, pady=0 , command=lambda: button_click(button_9,fp,fs,lbl_status,9))
	button_1.grid(row=0,column=0)
	button_2.grid(row=0,column=1)
	button_3.grid(row=0,column=2)
	button_4.grid(row=1,column=0)
	button_5.grid(row=1,column=1)
	button_6.grid(row=1,column=2)
	button_7.grid(row=2,column=0)
	button_8.grid(row=2,column=1)
	button_9.grid(row=2,column=2)
	

		
def clicked_rb(rb_val ,f,l ,r1,r2, o, fp,fs):
	global player1_choice , player2_choice, turn
	#print(f"Inside clicked_rb: rb_val received : {rb_val} data type = {type(rb_val)}")
	player1_choice=str(rb_val)
	if player1_choice=='1':
		player2_choice='0'
	elif player1_choice=='0':
		player2_choice='1'
	
	#print(f"Player-1 Choice : {player1_choice}")
	#print(f"Player-2 Choice : {player2_choice}")
	l.grid_forget()
	r1.grid_forget()
	r2.grid_forget()
	o.grid_forget()
	label_choice = Label(f,text= "player1_choice: "+player1_choice+"\nplayer2_choice: "+player2_choice)
	label_choice.grid(row=0,column=0,rowspan=2,columnspan=3)
	turn="Player-1"
	game_start(fp,fs)
			

	
	
		
def pass_info(*args):
	frame_head =Frame(root, bg='light yellow' ,bd=0)
	frame_head.place(relx=0.5, rely=0.01, relwidth=0.99, relheight=0.11, anchor='n')
	"""
	t=""
	for x in args:
		t+=" "+x
		t=t.strip()
	"""
	t=args[0]
	label_mesg = Label(frame_head,text=t)
	label_mesg.grid(row=0,column=0,columnspan=2)
	if len(args)>1:
		if args[1]=="NEW":
			rb1=Radiobutton(frame_head, text="Option 1", variable=r, value=1, anchor='n' )
			rb1.grid(row=1,column=0,columnspan=1)
			rb2=Radiobutton(frame_head, text="Option 2", variable=r, value=0, anchor='n' )
			rb2.grid(row=1,column=1,columnspan=1)
			
	opt_select = Button(frame_head,text="Confirm \n Option" ,command= lambda: clicked_rb(r.get(),frame_head,label_mesg ,rb1,rb2,opt_select,frame_pad,frame_status))
	opt_select.grid(row=0,column=2,rowspan=2 , padx=0,pady=0)	
	
	frame_pad =Frame(root, bg='light green' ,bd=0)
	frame_pad.place(relx=0.5, rely=0.13, relwidth=0.99, relheight=0.75 , anchor='n')
	frame_status =Frame(root, bg='light yellow' ,bd=0)
	frame_status.place(relx=0.5, rely=0.88, relwidth=0.99, relheight=0.12, anchor='n')

	
	
		
	
file_menu = Menu(my_menu)

my_menu.add_cascade(label='File', menu=file_menu)

file_menu.add_command(label='New..', command=file_new)
file_menu.add_separator()
file_menu.add_command(label='Exit', command=quit_app)


"""
#file_menu.add_cascade(label='File', menu=file_menu)

edit_menu = Menu(my_menu)
my_menu.add_cascade(label='Edit', menu=edit_menu)
edit_menu.add_command(label='Cut', command=lambda:pass_info("Edit-->Cut Selected"))
edit_menu.add_command(label='Copy', command=lambda:pass_info("Edit-->Copy Selected"))

option_menu = Menu(my_menu)

my_menu.add_cascade(label='Options', menu=option_menu)
option_menu.add_command(label='Find', command= lambda:pass_info("Option-->Find Selected"))
option_menu.add_command(label='Replace', command= lambda : pass_info("Option-->Replace Selected"))
"""
root.resizable(False, False) 
root.mainloop()
#root.destroy()
