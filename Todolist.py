import datetime
import time
import sys
print('\n \tHello User, I`m your schedule and to do assistant... You can always tell what`s on your to do list, I`ll save it for you and I`ll remind you whenever you ask me\n')
time.sleep(2)

#append add write a new or exidting file
def appending(num):
		global name
		name= unique
		global schedule
		schedule= input('Enter the future event you want to add to your todo list\n')
		global when
		when=input(f'enter the time you want to do it in the format `hr:min` make sure to use the 24hours format\n')
		global day
		day=input('enter date you want to doin the format `dd/mm`\n')
		add='\n' + schedule+ ' on ' + day +' by ' +when
		with open(name, "a+") as f:
				f.writelines(add)
				f.close()
				print('Your to do list has been saved')
				time.sleep(2)
				check= input('do you want to check your todo list,yes or no?\n')
				try:
					if check=='yes':
						with open(name, 'r') as f:
							stored_2= f.read()
							print(stored_2,'\n')
							f.close()
					elif check== 'no':
						print('Okay i`ll remind you later, your todo list has been saved')
					else:
						raise NameError
				except NameError:
					print('you have entered the wrong command')
		

""" check if a person already has a file saved in his name"""
unique=input('Enter your name, let me check if your todo list has been created before\n').lower()
try:
	with open(unique, 'r') as g:     #check if file exists and read it
					found=g.read()
					print(f'{unique} you have a todo list already')
					time.sleep(2)
					option=input('Do you want to see it, yes or no?\n').lower()
					if option=='yes':
						print('Here is your todo list\n')
						print(found,'\n')
						time.sleep(2)
						append=input('do you want to add more schedules to your list, yes or no\n').lower()
						if append=='yes':
							num = int(input('how many list do you want to append?\n'))
							for i in range(num):
								appending(num)
							quit()
						else:
							print('your todo list is intact')
							sys.exit()
					elif option=='no':
						print('Okay bye...')
						quit()
					else:
						print('Follow instructions')
	raise FileNotFoundError   #if file is not found
except FileNotFoundError:
				name= unique
				print(f'I couldn`t find a todo list that belongs to {name} , I will create one for you\n')
	

time.sleep(2)

num = int(input('how many schedule do you want add to your to do lidt ?\n'))
time.sleep(2)

print(f'Enter  your todo list in the format below,so i can save it for you\n ')


for i in range(num):
	appending(num)
	
s_time= datetime.datetime.now()
curr_time= s_time.strftime('%H:%M')
curr_date= s_time.strftime('%d/%m')
if curr_date==day and curr_time== when:
		print(f" *  *		 *  *		***********                    				  	  *  *		 *  *		***	  ***									 	  *  *   *    *  *		 	*	 *										 	  *  *   *    *  *			 *     * 										 	  *  *		 *  *		  ***	***								 		  *  *		 *  *	    **********					Reminder!!! {name}, {schedule} is due!!!") #where alarm is supposed to be
elif curr_date==day and curr_time< when:
		print("Time has elapsed!, add future events only")
else:
	print('Not yet due')		
	
	
# I couldn't add the alarm  part 
