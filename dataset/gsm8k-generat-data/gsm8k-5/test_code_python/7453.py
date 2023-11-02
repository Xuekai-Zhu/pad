def solution():
    james_friends = 75  # James has 75 friends
    john_friends = 3 * james_friends  # John has 3 times as many friends as James
    shared_friends = 25  # They share 25 friends

    # Calculate the total number of friends on their combined list
    total_friends = james_friends + john_friends - shared_friends
    result = total_friends
    return result

print(solution())