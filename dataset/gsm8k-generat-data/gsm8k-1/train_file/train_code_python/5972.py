def solution():
    """Nathaniel has 11 tickets to a basketball game. He gives away 2 tickets each to his best friends, until he only has 3 tickets left. How many best friends does Nathaniel have?"""
    starting_tickets = 11
    remaining_tickets = 3
    tickets_given_per_friend = 2
    friends_given_to = (starting_tickets - remaining_tickets) / tickets_given_per_friend
    result = friends_given_to
    return result

print(solution())