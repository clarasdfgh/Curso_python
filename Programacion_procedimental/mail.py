def check_email(email):
	return ("@" in email) and email.endswith(".com")

mail = input("Introduzca el email: ")

print(check_email(mail))
