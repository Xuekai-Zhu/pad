def solution():
    """If the sum of two numbers is 33, and if the second number is twice the first number, what is the second number?"""
    # Define variables
    first_number = 0
    second_number = 0

    # Set up system of equations
    # x + y = 33
    # y = 2x

    # Solve for x
    first_number = (33 / 3) # x = (33 - y) / 2

    # Solve for y
    second_number = 2 * first_number

    # Display the second number
    result = second_number
    return result

print(solution())