def solution():
    # First and second numbers are the same, so they must be 2
    first_digit = 2
    second_digit = 2

    # Third number is zero
    third_digit = 0

    # Fourth number is double the first number
    fourth_digit = 2 * first_digit

    # Fourth and fifth numbers add up to 8, so fifth number is 8 - fourth number
    fifth_digit = 8 - fourth_digit

    # Check that the sum of all digits is 10
    if (first_digit + second_digit + third_digit + fourth_digit + fifth_digit) == 10:
        result = str(first_digit) + str(second_digit) + str(third_digit) + str(fourth_digit) + str(fifth_digit)
    else:
        result = "No valid zip code exists."

    return result

print(solution())