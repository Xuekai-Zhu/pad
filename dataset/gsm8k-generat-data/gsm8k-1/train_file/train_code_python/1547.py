def solution():
    """Bill is trying to control the pests in his garden. Each spider he introduces eats 7 bugs, and each time he sprays the garden he reduces the total bug population to 80% of what it was previously. If the garden has 400 bugs to start, and Bill sprays once and introduces 12 spiders, how many bugs are left?"""
    initial_bugs = 400
    spiders = 12
    bugs_eaten_per_spider = 7
    total_bugs_eaten = spiders * bugs_eaten_per_spider
    bugs_after_spraying = initial_bugs * 0.8
    bugs_left = bugs_after_spraying - total_bugs_eaten
    result = bugs_left
    return result

print(solution())