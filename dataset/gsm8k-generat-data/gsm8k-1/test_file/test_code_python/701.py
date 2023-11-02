def solution():
    """Martha's cat is 5 times faster than her turtle. If the cat can run 15 feet/second, how many feet can her turtle crawl in 40 seconds?"""
    cat_speed = 15
    turtle_speed = cat_speed / 5
    time = 40
    distance = turtle_speed * time
    result = distance
    return result

print(solution())