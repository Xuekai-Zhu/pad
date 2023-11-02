def solution():
    
    initial_bugs = 400
    spiders = 12
    bugs_eaten_per_spider = 7
    total_bugs_eaten = spiders * bugs_eaten_per_spider
    bugs_after_spraying = initial_bugs * 0.8
    bugs_left = bugs_after_spraying - total_bugs_eaten
    result = bugs_left
    return result

print(solution())