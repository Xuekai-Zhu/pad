def solution():
    """Travis and his brother joined a trick-or-treat event. They collected 68 pieces of candy altogether. Each of them ate 4 pieces of candy after the event. How many pieces of candy were left?"""
    # Define the total number of candy collected
    total_candy = 68

    # Calculate the number of candy they ate
    candy_ate = 4 * 2

    # Calculate the number of candy left
    candy_left = total_candy - candy_ate

    # return the result
    result = candy_left
    return result

print(solution())