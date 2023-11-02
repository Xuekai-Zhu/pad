def solution():
    num_marbles = 500
    num_friends = 4
    marbles_given = num_friends * 80

    # Calculate the number of marbles remaining
    marbles_remaining = num_marbles - marbles_given

    # Calculate four times the number of marbles remaining
    result = 4 * marbles_remaining
    return result

print(solution())