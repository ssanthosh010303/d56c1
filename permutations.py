# Author: Apache X692 Attack Helicopter
# Created on: 27/06/2024
#
# String Permutations
def permutations(s):
    result = []

    def permute(s, current):
        if len(s) == 0:
            result.append(current)
        else:
            for i in range(len(s)):
                next_char = s[i]
                remaining_chars = s[:i] + s[i+1:]
                permute(remaining_chars, current + next_char)

    permute(s, "")
    return result

def main():
    input_string = input("Enter a string: ")
    perms = permutations(input_string)

    print("\nPermutations:")
    for perm in perms:
        print(perm)

if __name__ == "__main__":
    main()
