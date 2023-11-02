def solution():
    """A survey conducted by the school showed that only 20% of the 800 parents agree to a tuition fee increase. How many parents disagree with the tuition fee increase?"""
    total_parents = 800
    agree_percent = 20
    disagree_percent = 100 - agree_percent
    disagree_num = (disagree_percent / 100) * total_parents
    result = disagree_num
    return result

print(solution())