def solution():
    # Define initial number of marbles
    initial_marbles = 100

    # Keep 20 marbles
    remaining_marbles = initial_marbles - 20

    # Divide remaining marbles among 5 friends
    marbles_per_friend = remaining_marbles / 5
    result = marbles_per_friend
    return result

print(solution())