def solution():
    num_tickets = 11
    num_given_away = 0
    num_left = 3

    # Keep giving away tickets until only 3 are left
    while num_tickets > num_left:
        num_tickets -= 2
        num_given_away += 2

    # Calculate the number of best friends Nathaniel has
    num_best_friends = num_given_away / 2
    result = num_best_friends
    return result

print(solution())