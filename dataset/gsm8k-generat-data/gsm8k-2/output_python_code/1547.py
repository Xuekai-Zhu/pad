def solution():
    """Bill is trying to control the pests in his garden. Each spider he introduces eats 7 bugs, and each time he sprays the garden he reduces the total bug population to 80% of what it was previously. If the garden has 400 bugs to start, and Bill sprays once and introduces 12 spiders, how many bugs are left?"""
    starting_bugs = 400
    spider_eats = 7
    sprayed_bugs = starting_bugs * 0.8
    introduced_spiders = 12
    total_spider_eats = introduced_spiders * spider_eats
    remaining_bugs = sprayed_bugs - total_spider_eats
    result = remaining_bugs
    return result

print(solution())