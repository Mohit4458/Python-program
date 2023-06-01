def is_prime(num):

    if num <= 1:

        return False

    # Check for factors from 2 to the square root of the number

    for i in range(2, int(num**0.5) + 1):

        if num % i == 0:

            return False

    return True

# Prompt the user for input

number = int(input("Enter a number: "))

if is_prime(number):

    print(number, "is a prime number.")

else:

    print(number, "is not a prime number.")

