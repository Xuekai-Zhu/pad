def solution():
    """Betty has a tray of cookies and a tray of brownies. She has a real sweet tooth and eats 3 cookies a day and 1 brownie a day. If she starts with 60 cookies and 10 brownies, how many more cookies than brownies does she have after a week of eating like this?"""
    cookies_per_day = 3
    brownies_per_day = 1
    days_per_week = 7
    starting_cookies = 60
    starting_brownies = 10
    cookies_left = starting_cookies - (cookies_per_day * days_per_week)
    brownies_left = starting_brownies - (brownies_per_day * days_per_week)
    difference = cookies_left - brownies_left
    result = difference
    return result

print(solution())