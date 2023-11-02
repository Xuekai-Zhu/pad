def solution():
    initial_friends = 20  # James starts with 20 friends
    lost_friends = 2  # James lost 2 friends after an argument at work
    gained_friends = 1  # James made 1 friend on his way back home

    # Calculate the total number of friends James has after losing and gaining some friends
    remaining_friends = initial_friends - lost_friends + gained_friends
    result = remaining_friends
    return result

print(solution())