def solution():
    """Jerry is writing a script for a skit with three characters. The first character has eight more lines than the second character. The third character only has two lines. The second character has six more than three times the number of lines the third character has. How many lines does the first character in Jerry’s skit script have?"""
    # Define the number of lines for the third character
    lines_3 = 2

    # Calculate the number of lines for the second character
    lines_2 = 3 * lines_3 + 6

    # Calculate the number of lines for the first character
    lines_1 = lines_2 + 8

    # Display the number of lines for the first character
    result = lines_1
    return result

print(solution())