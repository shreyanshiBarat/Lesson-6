
char = input("Enter a character: ")

if len(char) == 1:
    if char.isalpha():
        print(f"'{char}' is an alphabet.")
    else:
        print(f"'{char}' is NOT an alphabet.")
else:
    print("Please enter only one character.")
