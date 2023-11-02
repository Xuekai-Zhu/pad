def solution():
    """Nina enjoys keeping insects as pets. She has 3 spiders and 50 ants. Each spider has 8 eyes. Each ant has 2 eyes. How many eyes are there in total among Nina’s pet insects?"""
    # Calculate the total number of eyes on the spiders
    spider_eyes = 3 * 8

    # Calculate the total number of eyes on the ants
    ant_eyes = 50 * 2

    # Calculate the total number of eyes on all of Nina's pet insects
    total_eyes = spider_eyes + ant_eyes

    result = total_eyes
    return result

print(solution())