def solution():
    # Calculate how many marbles are in each bag
    marbles_per_bag = 28 // 4  # The // operator is used for integer division

    # Calculate how many marbles James gave away
    marbles_given_away = marbles_per_bag

    # Calculate how many marbles James has left
    marbles_left = 28 - marbles_given_away

    result = marbles_left
    return result

print(solution())