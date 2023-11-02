def solution():
    """Betty has a tray of cookies and a tray of brownies. She has a real sweet tooth and eats 3 cookies a day and 1 brownie a day. If she starts with 60 cookies and 10 brownies, how many more cookies than brownies does she have after a week of eating like this?"""
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