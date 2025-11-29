# Password generator

import string
import secrets

Password_chars = string.ascii_letters + string.punctuation + string.digits

def password_generator(length):
  
    return "".join(secrets.choice(Password_chars) for _ in range(length))


def main():
    print("=" * 40)
    print(" Welcome To The Password Generator!")
    print("=" * 40)

    attempts_left = 5

    while attempts_left > 0:
        print(f"\nAtttempts Left: {attempts_left}")
        print("\n1. Generate Password")
        print("\n2. Exit")

        choice = input("\nYour Choice: ")

        if choice == "1":
            try:
                length = int(input("Enter the Password Length (8-32): "))
                if length < 8 or length > 32:
                    print("Length Must Be Between 8-32!")
                    continue
                password = password_generator(length)
                print(f"\n Your Password : {password}")

                attempts_left -= 1
                if attempts_left == 0:
                    print("\n Daily Limit reached! Come back tomorrow")

            except ValueError:
                print("Please inout a valid number!")

        elif choice == "2":
            print("\n Goodbye!")
            break

        else:
            print("Invalid choice!")

if __name__  == "__main__":
    main()
