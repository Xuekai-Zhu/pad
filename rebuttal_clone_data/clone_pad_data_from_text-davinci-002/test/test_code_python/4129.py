def solution():
    cookies_per_day = 3
    brownies_per_day = 1
    days_in_week = 7
    initial_cookies = 60
    initial_brownies = 10
    cookies_eaten = cookies_per_day * days_in_week
    brownies_eaten = brownies_per_day * days_in_week
    remaining_cookies = initial_cookies - cookies_eaten
    remaining_brownies = initial_brownies - brownies_eaten
    cookie_advantage = remaining_cookies - remaining_brownies
    result = cookie_advantage
    
    return result

print(solution())