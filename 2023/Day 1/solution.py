data = open("input.txt")
sum = 0
alpha_digits = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

for line in data:
    first_digit_flag = True

    for x in alpha_digits:
        if x in line:
            line = line.replace(x, x[0] + alpha_digits[x] + x[-1])

    for char in line:
        if(char.isnumeric() and first_digit_flag):
            first_digit = char
            last_digit = char
            first_digit_flag = False

        elif(char.isnumeric()):
            last_digit = char

    number = first_digit + last_digit
    sum += int(number)
    
print(sum)
data.close()