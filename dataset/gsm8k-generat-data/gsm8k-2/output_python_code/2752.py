def solution():
    """Nina enjoys keeping insects as pets. She has 3 spiders and 50 ants. Each spider has 8 eyes. Each ant has 2 eyes. How many eyes are there in total among Nina’s pet insects?"""
    spider_eyes = 8
    ant_eyes = 2
    total_spider_eyes = 3 * spider_eyes
    total_ant_eyes = 50 * ant_eyes
    total_eyes = total_spider_eyes + total_ant_eyes
    result = total_eyes
    return result

print(solution())