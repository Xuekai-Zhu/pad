def solution():
    """An entrepreneur is crowdfunding a new business effort. He has three different dollar amount levels of financial backing options and each level is ten times as high as the previous one. He needs to raise $12000 to get his business off the ground. He succeeded after getting two backers at the highest level of financial backing, three at the second level, and ten at the lowest level. How many dollars was the highest level of financial backing?"""
    total_backers = 2 + 3 + 10
    total_amount = 12000
    lowest_level_amount = total_amount / (10**2 + 10**1 + 1)
    highest_level_amount = lowest_level_amount * (10**2)
    result = highest_level_amount
    return result

print(solution())