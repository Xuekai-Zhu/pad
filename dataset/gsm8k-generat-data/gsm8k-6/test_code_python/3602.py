def solution():
    # Calculate the total number of cookies eaten by Jackson's sons each day
    cookies_per_day = 4 + 2  # oldest son gets 4 cookies, youngest son gets 2 cookies

    # Calculate the number of days the box of cookies will last
    days = 54 // cookies_per_day  # integer division gives the number of full days the box will last
    result = days
    return result

print(solution())