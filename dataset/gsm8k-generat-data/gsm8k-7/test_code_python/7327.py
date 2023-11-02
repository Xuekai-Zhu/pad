def solution():
    initial_cookies = 60
    initial_brownies = 10
    cookies_per_day = 3
    brownies_per_day = 1
    days = 7

    # Calculate the total number of cookies and brownies consumed in a week
    cookies_consumed = cookies_per_day * days
    brownies_consumed = brownies_per_day * days

    # Calculate the remaining cookies and brownies after a week
    remaining_cookies = initial_cookies - cookies_consumed
    remaining_brownies = initial_brownies - brownies_consumed

    # Calculate the difference between remaining cookies and remaining brownies
    difference = remaining_cookies - remaining_brownies
    result = difference
    return result

print(solution())