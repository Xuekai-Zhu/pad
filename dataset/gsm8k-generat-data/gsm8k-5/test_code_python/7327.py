def solution():
    cookies_per_day = 3  # Betty eats 3 cookies per day
    brownies_per_day = 1  # Betty eats 1 brownie per day
    starting_cookies = 60  # Betty starts with 60 cookies
    starting_brownies = 10  # Betty starts with 10 brownies
    days = 7  # Betty eats like this for 7 days

    # Calculate the total number of cookies and brownies eaten in a week
    total_cookies_eaten = cookies_per_day * days
    total_brownies_eaten = brownies_per_day * days

    # Calculate the remaining number of cookies and brownies
    remaining_cookies = starting_cookies - total_cookies_eaten
    remaining_brownies = starting_brownies - total_brownies_eaten

    # Calculate the difference between the remaining cookies and brownies
    difference = remaining_cookies - remaining_brownies
    result = difference
    return result

print(solution())