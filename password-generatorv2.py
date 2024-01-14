import random
import string 

password_generate = ''


def password_length_size_loop():
	while True:
		try: 
			password_length_size = int(input("Enter password length: "))
			return password_length_size
		except ValueError:
			print("Invalid input. Please enter a number")

def yes_no_input_loop(prompt):
	while True:
		try:
			user_input = input(prompt).lower()
			if user_input in ['y', 'n']:
				return user_input
			else:
				print("Invalid input. Please enter 'y' or 'n'.")
		except ValueError:
			print("Invalid input. Please enter 'y' or 'n'.")


def generate_password(length, use_numbers, use_uppercase, use_lowercase, use_symbols):
	characters = ''
	if use_numbers:
		characters += string.digits
	if use_uppercase:
		characters += string.ascii_uppercase
	if use_lowercase:
		characters += string.ascii_lowercase
	if use_symbols:
		characters += string.punctuation

	if not characters:
		print("No characters types selected. Cannot generate password.")
		return None

	return ''.join(random.choice(characters) for _ in range(length))

def main_menu():
	while True:
		print('******Password Generator*******')
		print('Choose Option')
		print('1: Generate Password')
		print('2: Exit the program')

		user_choice = input('Your Choice: ') 

		if user_choice == '1':
			password_length = password_length_size_loop()
			use_numbers = yes_no_input_loop("Use numbers? (y/n): ") == 'y'
			use_uppercase = yes_no_input_loop("Use uppercase letters? (y/n): ") == 'y'
			use_lowercase = yes_no_input_loop("Use lowercase letters? (y/n): ") == 'y'
			use_symbols = yes_no_input_loop("Use symbols? (y/n): ") == 'y'

			generated_password = generate_password(password_length, use_numbers, use_uppercase, use_lowercase, use_symbols)

			if generate_password:
				print("Generated Password is:", generated_password)

		elif user_choice == '2':
			print('Exiting the Program.')
			print('Goodye!')
			break
		else:
			print('####### Invalid Choice. Please enter 1 or 2. #######')

main_menu()