import random


digits = '0123456789'
symbols = '!@#$%&*><'
lowercase_letters = 'abcdefghijklmonpqrstuvwxyz'
uppercase_letters = lowercase_letters.upper()
all_characters = digits + symbols + lowercase_letters + uppercase_letters
no_digits = symbols + lowercase_letters + uppercase_letters
no_symbols = digits + lowercase_letters + uppercase_letters
no_uppercase = digits + symbols + lowercase_letters
symbols_and_lowercase = symbols + lowercase_letters
only_digits = digits+lowercase_letters
only_uppercase = uppercase_letters + lowercase_letters
only_symbols = symbols + lowercase_letters



def generate_password():
	password_length_size = int(input("Enter password length: "))
	uppercase_letters = input("Use uppercase letters? (y/n): ")
	use_numbers = input("Use digits? (y/n): ")
	use_spec_char = input("Use special characters? (y/n): ")

	password = ''


	if (uppercase_letters == 'y' or uppercase_letters == 'Y') and (use_numbers == 'y' or use_numbers == 'Y') and (use_spec_char == 'y' or use_spec_char == 'Y'):
		for char in range(password_length_size):
			password += random.choice(all_characters)
		return password
		

	elif (uppercase_letters == 'n' or uppercase_letters == 'N') and (use_numbers == 'y' or use_numbers == 'Y') and (use_spec_char == 'y' or use_spec_char == 'Y'):
		for char in range(password_length_size):
			password += random.choice(no_uppercase)
		return password
	

	elif (uppercase_letters == 'y' or uppercase_letters == 'Y') and (use_numbers == 'n' or use_numbers == 'N') and (use_spec_char == 'y' or use_spec_char == 'Y'):
		for char in range(password_length_size):
			password += random.choice(no_digits)
		return password
	

	elif (uppercase_letters == 'y' or uppercase_letters == 'Y') and (use_numbers == 'y' or use_numbers == 'Y') and (use_spec_char == 'n' or use_spec_char == 'N'):
		for char in range(password_length_size):
			password += random.choice(no_symbols)
		return password
		

	elif (uppercase_letters == 'n' or uppercase_letters == 'N') and (use_numbers == 'n' or use_numbers == 'N') and (use_spec_char == 'y' or use_spec_char == 'Y'):
		for char in range(password_length_size):
			password += random.choice(only_symbols)
		return password
		

	elif (uppercase_letters == 'n' or uppercase_letters == 'N') and (use_numbers == 'y' or use_numbers == 'Y') and (use_spec_char == 'n' or use_spec_char == 'N'):
		for char in range(password_length_size):
			password += random.choice(only_digits)
		return password
		

	elif (uppercase_letters == 'y' or uppercase_letters == 'Y') and (use_numbers == 'n' or use_numbers == 'N') and (use_spec_char == 'n' or use_spec_char =='N'):
		for char in range(password_length_size):
			password += random.choice(only_uppercase)
		return password
	
	else:
		for char in range(password_length_size):
			password += random.choice(lowercase_letters)
		return password




password_generate = ''


def password_length_size_loop():
	while True:
		try:
			password_length_size = int(input("Enter password length: "))
			break
		except ValueError:
			print("Invalid Input. Please enter a number")



def numbers_loop():
	while True:
		try:
			numbers_check = input("Use uppercase letters? (y/n): ")
		except ValueError:	
			print("Invalid input. Please enter 'y' or 'n'.")
		else:
			if numbers_check.lowercase() == 'y' or numbers_check.lowercase() == 'n':
				break
			else:
				print("Invalid input. Please enter 'y' or 'n'.")



def uppercase_letters_loop():
	while True:
		try:
			uppercase_letters_check = input("Use uppercase letters? (y/n): ")
		except ValueError:	
			print("Invalid input. Please enter 'y' or 'n'.")
		else:
			if uppercase_letters_check.lowercase() == 'y' or uppercase_letters_check.lowercase() == 'n':
				break
			else:
				print("Invalid input. Please enter 'y' or 'n'.")



def lowercase_letters_loop():
	while True:
		try:
			lowercase_letters_check = input("Use uppercase letters? (y/n): ")
		except ValueError:	
			print("Invalid input. Please enter 'y' or 'n'.")
		else:
			if lowercase_letters_check.lowercase() == 'y' or lowercase_letters_check.lowercase() == 'n':
				break
			else:
				print("Invalid input. Please enter 'y' or 'n'.")



def symbols_loop():
	while True:
		try:
			symbols_check = input("Use uppercase letters? (y/n): ")
		except ValueError:	
			print("Invalid input. Please enter 'y' or 'n'.")
		else:
			if symbols_check.lowercase() == 'y' or symbols_check.lowercase() == 'n':
				break
			else:
				print("Invalid input. Please enter 'y' or 'n'.")





def main_menu():

	while True:
		print('*****Password Generator*****')
		print('Choose Option')
		print('1: Generate Password')
		print('2: Exit the Program')

		user_choice = input('Your Choice: ')
	

		if user_choice == '1':
#			print(generate_password())
			print(password_length_size_loop())
			if password_length_size_loop() == False:
				print(numbers_loop())
				


		elif user_choice == '2':
			print('Exiting the Program.')
			print('Goodbye!')
			break
		else:
			print('#######Invalid Choice. Please enter 1 or 2.#######')






main_menu()

#print(generate_password())