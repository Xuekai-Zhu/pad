def solution():
    """Nathaniel has 11 tickets to a basketball game. He gives away 2 tickets each to his best friends, until he only has 3 tickets left. How many best friends does Nathaniel have?"""
    # Define the initial number of tickets and the number of tickets given away each time
    initial_tickets = 11
    given_away = 2

    # Initialize the number of friends given tickets to
    friends_given_tickets = 0

    # Give away tickets until there are only 3 left
    while initial_tickets > 3:
        initial_tickets -= given_away
        friends_given_tickets += 1

    # Display the number of friends given tickets to
    result = friends_given_tickets
    return result

print(solution())