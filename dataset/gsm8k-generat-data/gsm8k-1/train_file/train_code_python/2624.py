def solution():
    """55% of Toby's friends are boys and the rest are girls. If he has 33 friends who are boys, how many friends does he have who are girls?"""
    total_friends = 100
    boys_percent = 55
    boys_friends = 33
    girls_percent = 100 - boys_percent
    girls_friends = total_friends - boys_friends
    boys_ratio = boys_friends / (boys_friends + girls_friends)
    girls_ratio = 1 - boys_ratio
    girls_friends = girls_ratio * total_friends
    result = girls_friends
    return result

print(solution())