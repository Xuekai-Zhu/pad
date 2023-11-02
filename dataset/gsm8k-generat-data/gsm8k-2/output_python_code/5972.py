def solution():
    """Nathaniel has 11 tickets to a basketball game. He gives away 2 tickets each to his best friends, until he only has 3 tickets left. How many best friends does Nathaniel have?"""
    tickets = 11
    friends = 0
    while tickets >= 3:
        tickets -= 2
        friends += 1
    result = friends
    return result

print(solution())