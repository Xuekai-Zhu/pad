def solution():
    """Jerry is writing a script for a skit with three characters. The first character has eight more lines than the second character. The third character only has two lines. The second character has six more than three times the number of lines the third character has. How many lines does the first character in Jerry’s skit script have?"""
    # Define the number of lines for the third character
    third_character = 2

    # Calculate the number of lines for the second character
    second_character = 3 * third_character + 6

    # Calculate the number of lines for the first character
    first_character = second_character + 8

    # return the result
    result = first_character
    return result

print(solution())