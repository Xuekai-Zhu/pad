def solution():
    # Define the number of cookies and brownies eaten per day
    cookies_per_day = 3
    brownies_per_day = 1

    # Define the initial number of cookies and brownies
    initial_cookies = 60
    initial_brownies = 10

    # Calculate the number of cookies and brownies left after a week of eating like this
    cookies_left = initial_cookies - 7 * cookies_per_day
    brownies_left = initial_brownies - 7 * brownies_per_day

    # Calculate the difference between the number of cookies and brownies left
    difference = cookies_left - brownies_left
    result = difference
    return result

print(solution())