def solution():
    """Nina enjoys keeping insects as pets. She has 3 spiders and 50 ants. Each spider has 8 eyes. Each ant has 2 eyes. How many eyes are there in total among Nina’s pet insects?"""
    spider_count = 3
    ant_count = 50
    spider_eye_count = 8
    ant_eye_count = 2
    total_spider_eyes = spider_count * spider_eye_count
    total_ant_eyes = ant_count * ant_eye_count
    total_eyes = total_spider_eyes + total_ant_eyes
    result = total_eyes
    return result

print(solution())