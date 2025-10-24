# Use get() and setdefault() for safe key access.

user={'name': 'Jak'}
age=user.get('age',28)
user.setdefault('city', 'Dhaka')
if __name__ == '__main__':
 print("User Dictionary: ",user)
 print("Age (default if missing): ",age)