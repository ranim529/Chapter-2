import re

email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
email = input("Enter an email address to validate: ")

if re.match(email_pattern, email):
    print(f"'{email}' valid")
else:
    print(f"'{email}' not valid")
