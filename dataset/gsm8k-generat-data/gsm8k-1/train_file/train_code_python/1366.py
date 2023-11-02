def solution():
    """An entrepreneur is crowdfunding a new business effort. He has three different dollar amount levels of financial backing options and each level is ten times as high as the previous one. He needs to raise $12000 to get his business off the ground. He succeeded after getting two backers at the highest level of financial backing, three at the second level, and ten at the lowest level. How many dollars was the highest level of financial backing?"""
    goal = 12000
    backers_lowest_level = 10
    backers_second_level = 3
    backers_highest_level = 2
    total_backers = backers_lowest_level + backers_second_level + backers_highest_level
    highest_level_amount = goal / (backers_lowest_level + backers_second_level + backers_highest_level * 10 + backers_highest_level * 100)
    result = highest_level_amount * 100
    
    return result

print(solution())