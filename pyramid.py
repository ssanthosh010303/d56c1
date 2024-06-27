# Author: Apache X692 Attack Helicopter
# Created on: 27/06/2024
#
# Pyramid Pattern
def print_pyramid(rows):
    for i in range(1, rows + 1):
        print(" " * (rows - i), end='')
        print("* " * i)

def main():
    rows = int(input("Enter the number of rows: "))
    print_pyramid(rows)

if __name__ == "__main__":
    main()
