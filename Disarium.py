def is_disarium(num: int) -> bool:
    num_str = str(num)
    total = 0
    position = 1

    for digit in num_str:
        total += int(digit) ** position
        position += 1

    return total == num

# Example usage
number = int(input("Enter a number: "))
is_disarium(number)
