def solution():
    """In Rodrigo's classroom in the morning there are red chairs, yellow chairs, and blue chairs. There are 4 red chairs.
    There are 2 times as many yellow chairs as red chairs, and there are 2 fewer blue chairs than yellow chairs.
    In the afternoon, Lisa borrows 3 chairs. How many chairs are left in Rodrigo's classroom?"""
    # Define the number of red chairs
    red_chairs = 4

    # Calculate the number of yellow chairs
    yellow_chairs = 2 * red_chairs

    # Calculate the number of blue chairs
    blue_chairs = yellow_chairs - 2

    # Calculate the total number of chairs before Lisa borrows three chairs
    total_chairs = red_chairs + yellow_chairs + blue_chairs

    # Calculate the total number of chairs after Lisa borrows three chairs
    total_chairs -= 3

    # return the result
    result = total_chairs
    return result


# Testing the function with the given example in the prompt
print(solution())  # Output: 19

print(solution())