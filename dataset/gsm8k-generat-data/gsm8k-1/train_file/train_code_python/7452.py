def solution():
    """James and John combine their friends lists. James has 75 friends. John has 3 times as many friends as James. They share 25 friends. How many people are on the combined list? """
    james_friends = 75
    john_friends = james_friends * 3
    shared_friends = 25
    total_friends = james_friends + john_friends - shared_friends
    result = total_friends
    return result

print(solution())