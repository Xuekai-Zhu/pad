def solution():
    """55% of Toby's friends are boys and the rest are girls. If he has 33 friends who are boys, how many friends does he have who are girls?"""
    boys_percent = 55
    boys_count = 33
    total_friends = boys_count / (boys_percent / 100)
    girls_count = total_friends - boys_count
    result = girls_count
    return result

print(solution())