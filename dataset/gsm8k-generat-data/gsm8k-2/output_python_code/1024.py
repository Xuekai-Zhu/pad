def solution():
    """A survey conducted by the school showed that only 20% of the 800 parents agree to a tuition fee increase. How many parents disagree with the tuition fee increase?"""
    total_parents = 800
    agree_parents = total_parents * 0.2
    disagree_parents = total_parents - agree_parents
    result = disagree_parents
    return result

print(solution())