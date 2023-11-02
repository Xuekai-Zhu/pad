def solution():
    """Nina enjoys keeping insects as pets. She has 3 spiders and 50 ants. Each spider has 8 eyes. Each ant has 2 eyes. How many eyes are there in total among Nina’s pet insects?"""
    # Define the number of spiders and ants
    spider_count = 3
    ant_count = 50

    # Calculate the total number of eyes
    spider_eye_count = spider_count * 8
    ant_eye_count = ant_count * 2
    total_eye_count = spider_eye_count + ant_eye_count

    # Display the total number of eyes
    result = total_eye_count
    return result

print(solution())