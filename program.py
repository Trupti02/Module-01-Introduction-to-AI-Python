def is_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(is_even_odd(int(input("Enter a number: "))))