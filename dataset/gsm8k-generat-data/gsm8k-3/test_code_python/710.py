def solution():
    """Travis and his brother joined a trick-or-treat event. They collected 68 pieces of candy altogether. Each of them ate 4 pieces of candy after the event. How many pieces of candy were left?"""
    # Define the number of pieces of candy collected and eaten
    candy_collected = 68
    candy_eaten = 4 * 2  # both Travis and his brother ate 4 pieces each

    # Calculate the number of pieces of candy left
    candy_left = candy_collected - candy_eaten

    # Display the number of pieces of candy left
    result = candy_left
    return result

print(solution())