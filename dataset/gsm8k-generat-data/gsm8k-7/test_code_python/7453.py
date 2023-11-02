def solution():
    james_friends = 75
    john_friends = 3 * james_friends
    shared_friends = 25

    # Calculate the total number of unique friends
    total_friends = james_friends + john_friends - shared_friends

    result = total_friends
    return result

print(solution())