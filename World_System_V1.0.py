import json
import os
import subprocess
import sys
import time
work_folder = str(os.getcwd())
work_name = str(sys.argv[0])
work_path = str(work_folder + "\\" + work_name)
user_name_path = work_folder + "\\files\\username.json"
user_password_path = work_folder + "\\files\\password.json"
disk_info_path = work_folder + "\\files\\disk.json"
disk_path = work_folder + "\\disk"
help_path = work_folder + "\\files\\help"
i = subprocess.call("color 0f", shell=True)
print("Welcome to World System v1.0! \nPlease enter your user name and password to log in.")
while_state = True
while while_state:
	input_user = input("Username:")
	try:
		with open(user_name_path) as file_object:
			all_user = json.load(file_object)
	except FileNotFoundError:
		print("The user file could not be found. You may have changed or deleted it.\nPlease run this program again after confirming that everything is correct.")
		while_state = False
		exit()
	else:
		if input_user in all_user:
			try:
				with open(user_password_path) as file_object:
					all_password = json.load(file_object)
			except FileNotFoundError:
				print("The user file could not be found. You may have changed or deleted it.\nPlease run this program again after confirming that everything is correct.")
				while_state = False
			else:
				input_password = input("Log in as:" + input_user + "\nPassword:")
				The_index_of_password = all_user.index(input_user)
				The_user_password = (all_password[The_index_of_password])
				if input_password == The_user_password:
					while_state = False
					break
				else:
					print("You may have entered an incorrect password!\nPlease try again.")
		else:
			print("This account was not found!\nPlease try again.")
i = subprocess.call("cls", shell=True)
print('Welcome to World System v1.0!\nEnter "help" to display all commands and descriptions.\n')
while True:
	command = input("command >")
	command_split = command.split()
	try:
		command_first = (command_split[0])
	except IndexError:
		print("Error: command cannot be empty.")
	else:
		if command_first == "changecolor":
			try:
				command_second = (command_split[1])
			except IndexError:
				print("Error: parameter cannot be empty.")
			else:
				if command_second == "/?":
					print("Error: invalid parameter.")
				else:
					color_command = "color " + command_second
					i = subprocess.call(color_command, shell=True)
		if command_first == "cleanscreen":
			i = subprocess.call("cls", shell=True)
		if command_first == "diskeditor":
			try:
				with open(disk_info_path,'r', encoding='UTF-8') as file_object:
					all_disk = json.load(file_object)
			except FileNotFoundError:
				print("The user file could not be found. You may have changed or deleted it.\nPlease run this program again after confirming that everything is correct.")
			else:
				try:
					command_second = (command_split[1])
				except IndexError:
					print("Error: parameter cannot be empty.")
				else:
					if command_second == "alldisk":
						print("These are information for all disks:")
						for key,value in all_disk.items():
							print(key+": "+str(value)+"MB")
					elif command_second == "add":
						try:
							command_third = (command_split[2])
						except IndexError:
							print("Error: parameter cannot be empty.")
						else:
							if all_disk["Remaining_space"] == "0":
								print("Error: insufficient disk space.")
							input_disk_space = input ("Space of the new disk(MB):")
							try:
								input_disk_space = eval(input_disk_space)
							except NameError:
								print("Error: invalid value.")
							except SyntaxError:
								print("Error: invalid value.")
							else:
								if input_disk_space > eval(all_disk["Remaining_space"]):
									print("Error: insufficient disk space.")
								else:
									The_remaining_space_of_disk = eval(all_disk["Remaining_space"]) - input_disk_space
									all_disk["Remaining_space"] = str(The_remaining_space_of_disk)
									new_user_name_all = command_third + "_all"
									new_user_free_space = str(input_disk_space - 1)
									new_user_free = command_third  + "_free"
									all_disk[new_user_name_all] = str(input_disk_space)
									all_disk[new_user_free] = new_user_free_space
									with open(disk_info_path, "w") as f:
										f.write(json.dumps(all_disk, ensure_ascii=False, indent=4, separators=(',', ':')))
									print("Complete.")
					elif command_second == "cleanall":
						confirm_state = input("Warning: this operation is irreversible. Are you sure you want to continue?\nY=YES N=NO:")
						if confirm_state == "Y":
							input_password = input("Enter your account password to confirm this operation again:")
							if input_password == The_user_password:
								all_disk.clear()
								all_disk["Remaining_space"] = "500"
								print(all_disk)
								with open(disk_info_path, "w") as f:
										f.write(json.dumps(all_disk, ensure_ascii=False, indent=4, separators=(',', ':')))
								print("Complete.")
							else:
								print("This is not the correct password. This operation cannot continue.")
						elif confirm_state == "N":
							print("The operation has been canceled.")
						else:
							print("Error: invalid parameter.")
					elif command_second == "delete":
						try:
							command_third = (command_split[2])
						except IndexError:
							print("Error: parameter cannot be empty.")
						else:
							disk_name_all = command_third + "_all"
							disk_name_free = command_third + "_free"
							try:
								all_disk.pop(disk_name_free)
							except KeyError:
								print("Error: invalid value.")
							else:
								delete_disk_space = eval(all_disk[disk_name_all])
								all_disk.pop(disk_name_all)
								the_remaining_space_of_disk = eval(all_disk["Remaining_space"]) + delete_disk_space
								all_disk["Remaining_space"] = str(the_remaining_space_of_disk)
								with open(disk_info_path, "w") as f:
									f.write(json.dumps(all_disk, ensure_ascii=False, indent=4, separators=(',', ':')))
								print("Complete.")
		if command_first == "fileeditor":
			try:
				command_second = (command_split[1])
			except IndexError:
				print("Error: parameter cannot be empty.")
			else:
				if command_second == "create":
					try:
						command_third = (command_split[2])
					except IndexError:
						print("Error: parameter cannot be empty.")
					else:
						file_name = str(disk_path + "\\" + command_third)
						f=open(file_name,'w')
						print("Complete.")
				if command_second == "add":
					try:
						command_third = (command_split[2])
					except IndexError:
						print("Error: parameter cannot be empty.")
					else:
						try:
							command_fourth = (command_split[3])
						except IndexError:
							print("Error: invalid text.")
						else:
							file_name = str(disk_path + "\\" + command_third)
							f = open(file_name, 'a')
							f.write(command_fourth)
							f.close()
				if command_second == "cover":
					try:
						command_third = (command_split[2])
					except IndexError:
						print("Error: parameter cannot be empty.")
					else:
						try:
							command_fourth = (command_split[3])
						except IndexError:
							print("Error: invalid text.")
						else:
							file_name = str(disk_path + "\\" + command_third)
							f = open(file_name, 'w')
							f.write(command_fourth)
							f.close()
				
		if command_first == "filereader":
			try:
				command_second = (command_split[1])
			except IndexError:
				print("Error: parameter cannot be empty.")
			else:
				file_path = str(disk_path + "\\" + command_second)
				try:
					with open(file_path) as file_object:
						content = file_object.read()
				except FileNotFoundError:
					print(file_path)
					print("Error: file not found.")
				else:
					print(content)
		if command_first == "filelist":
			for filepath,dirnames,filenames in os.walk(disk_path):
				for filename in filenames:
					print (filename)
					
		if command_first == "help":
			with open(help_path) as file_object:
				content = file_object.read()
				print(content)
		if command_first == "time":
			print(time.strftime("%Y-%m-%d" + " " + "%H:%M:%S", time.localtime()))
		if command_first == "usereditor":
			try:
				command_second = (command_split[1])
			except IndexError:
				print("Error: parameter cannot be empty.")
			else:
				if command_second == "adduser":
					try:
						command_third = (command_split[2])
					except IndexError:
						print("Error: parameter cannot be empty.")
					else:
						input_password = input("You are trying to create a new user.\nEnter your password to confirm this action:")
						if input_password == The_user_password:
							input_password = input("Please enter the password of the new user:")
							input_password_len = len(input_password)
							if str(input_password_len) == "0":
								print("Error: password cannot be empty.")
							elif input_password_len >= 50:
								print("Error: the password is too long. \nPasswords should be limited to 50 letters and numbers.")
							else:
								all_user.append(command_third)
								all_password.append(input_password)
								with open(user_name_path,"w") as file_object:
									json.dump(all_user,file_object)
								with open(user_password_path,"w") as file_object:
									json.dump(all_password,file_object)
								print("Complete.")
						else:
							print("Error: incorrect password.")
				if command_second == "deleteuser":
					try:
						command_third = (command_split[2])
					except IndexError:
						print("Error: parameter cannot be empty.")
					else:
						input_password = input("You are trying to delete a user.\nEnter your password to confirm this action:")
						if input_password == The_user_password:
							try:
								The_index_of_user = all_user.index(command_third)
							except ValueError:
								print("Error: parameter cannot be empty.")
							else:
								del (all_user[The_index_of_user])
								del(all_password[The_index_of_user])
								with open(user_name_path,"w") as file_object:
									json.dump(all_user,file_object)
								with open(user_password_path,"w") as file_object:
									json.dump(all_password,file_object)
								print("Complete.")
						else:
							print("Error: incorrect password.")
				if command_second == "userlist":
						print("These are all users:")
						for user in all_user:
							print(user)
			if command_first == "version":
				print("World System V1.0")
