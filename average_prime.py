# Author: Apache X692 Attack Helicopter
# Created on: 27/06/2024
#
# Average of Prime Numbers
def is_prime(num):
    if num <= 1:
        return False

    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False

    return True

def main():
    numbers = []
    prime_numbers = []

    for _ in range(10):
        num = int(input("Enter a number: "))
        numbers.append(num)

    for num in numbers:
        if is_prime(num):
            prime_numbers.append(num)

    if len(prime_numbers) > 0:
        avg_prime = sum(prime_numbers) / len(prime_numbers)

        print(f"\nPrime numbers are: {prime_numbers}")
        print(f"Average of prime numbers: {avg_prime}")
    else:
        print("No prime numbers found.")

if __name__ == "__main__":
    main()
