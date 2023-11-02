def solution():
    
    cookies = 60
    brownies = 10
    days = 7
    cookies_eaten = 3 * days
    brownies_eaten = 1 * days
    cookies_remaining = cookies - cookies_eaten
    brownies_remaining = brownies - brownies_eaten
    diff = cookies_remaining - brownies_remaining
    result = diff
    return result

print(solution())