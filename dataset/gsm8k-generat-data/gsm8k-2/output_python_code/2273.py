def solution():
    """James has 20 friends. Yesterday at work he got into an argument with 2 of his friends. Now he no longer considers them as friends. On his way back home, he made one more friend. So how many friends does James have left?"""
    starting_friends = 20
    lost_friends = 2
    gained_friends = 1
    remaining_friends = starting_friends - lost_friends + gained_friends
    result = remaining_friends
    return result

print(solution())