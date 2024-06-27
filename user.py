# Author: Apache X692 Attack Helicopter
# Created on: 27/06/2024
#
# User Data
import re
from datetime import datetime

def get_valid_name(prompt):
    while True:
        name = input(prompt)

        if name.isalpha():
            return name
        else:
            print("Please enter a valid name (letters only).")

def get_valid_age(prompt):
    while True:
        age_str = input(prompt)

        if age_str.isdigit():
            age = int(age_str)

            if age >= 0:
                return age
            else:
                print("Age cannot be negative.")
        else:
            print("Please enter a valid age (digits only).")

def get_valid_dob(prompt):
    while True:
        dob_str = input(prompt)

        try:
            dob = datetime.strptime(dob_str, "%Y-%m-%d")
            return dob.date()
        except ValueError:
            print("Please enter date in format YYYY-MM-DD.")

def get_valid_phone(prompt):
    while True:
        phone = input(prompt)

        if re.match(r'^\d{10}$', phone):
            return phone
        else:
            print("Please enter a valid 10-digit phone number.")

def main():
    print("Please enter your details:")

    name = get_valid_name("    Name: ")
    age = get_valid_age("    Age: ")
    dob = get_valid_dob("    Date of birth (YYYY-MM-DD): ")
    phone = get_valid_phone("    Phone number (10 digits): ")

    print("\nEntered details:")
    print(f"    Name: {name}")
    print(f"    Age: {age}")
    print(f"    Date of Birth: {dob}")
    print(f"    Phone number: {phone}")

if __name__ == "__main__":
    main()
