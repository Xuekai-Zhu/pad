def solution():
    
    starting_bugs = 400
    spider_eats = 7
    sprayed_bugs = starting_bugs * 0.8
    introduced_spiders = 12
    total_spider_eats = introduced_spiders * spider_eats
    remaining_bugs = sprayed_bugs - total_spider_eats
    result = remaining_bugs
    return result

print(solution())