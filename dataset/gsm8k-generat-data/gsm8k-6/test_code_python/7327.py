def solution():
    # Calculate the number of cookies and brownies left after a week of eating
    cookies_left = 60 - 3*7  # Betty eats 3 cookies a day for 7 days
    brownies_left = 10 - 1*7  # Betty eats 1 brownie a day for 7 days
    
    # Calculate the difference between the number of cookies and brownies
    diff = cookies_left - brownies_left
    result = diff
    return result

print(solution())