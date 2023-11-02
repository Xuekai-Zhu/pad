def solution():
    """Nathaniel has 11 tickets to a basketball game. He gives away 2 tickets each to his best friends, until he only has 3 tickets left. How many best friends does Nathaniel have?"""
    # Define the initial number of tickets and the number of tickets given away each time
    INITIAL_TICKETS = 11
    TICKETS_GIVEN = 2

    # Initialize the number of best friends
    best_friends = 0

    # Give away tickets until only 3 are left
    while INITIAL_TICKETS > 3:
        INITIAL_TICKETS -= TICKETS_GIVEN
        best_friends += 1

    # Display the number of best friends Nathaniel has
    result = best_friends
    return result

print(solution())