# Day 1, Star 1 asks you to sum a large number of calibration values. 
# Each value is a two-digit number derived from a line in a .txt document.
# The first digit in the number being the first digit in the line, whereas the second digit in the number is the last digit in the line

import re #imports regex

# Read the file
with open('calibrations.txt', 'r') as file:
    sum = 0
    for line in file:

        # Read the line
        print("The line is " + line)

        # Keep only digits
        numbersOnly = re.sub(r'[a-zA-Z]', '', line)
        print("The line is now " + numbersOnly)

        # Remove whitespace and record the first and last digit in the string as the first and second calibration value
        numbersOnly = numbersOnly.strip()
        firstDigit = str(numbersOnly[0])
        secondDigit = str(numbersOnly[-1])
        print("The first digit is " + firstDigit)
        print("The second digit is " + secondDigit)

        # Concatenate the two digits to make one value, then add them to the total sum
        calibration = firstDigit + secondDigit
        sum = sum + int(calibration)

    # Print the final sum of all calibration digits  
    print(sum)

