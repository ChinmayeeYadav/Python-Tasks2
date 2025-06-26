def int_to_roman(num: int) -> str:
    if not 1 <= num <= 3999:
        return "Number out of range (1–3999)"

    val = [
        1000, 900, 500, 400,
        100,  90,  50,  40,
        10,   9,   5,   4,  1
    ]
    syms = [
        'M', 'CM', 'D', 'CD',
        'C', 'XC', 'L', 'XL',
        'X', 'IX', 'V', 'IV', 'I'
    ]

    roman = ""
    for i in range(len(val)):
        count = num // val[i]
        roman += syms[i] * count
        num -= val[i] * count

    return roman

num = int(input("Enter number:"))
roman_num = int_to_roman(num)
print(roman_num)
