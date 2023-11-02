def solution():
    # Calculate the total number of cookies baked by Frank in 6 days
    total_cookies = 2 * 12 * 6  # Frank bakes two trays of 12 cookies per day for 6 days

    # Calculate the number of cookies eaten by Frank and Ted
    total_cookies_eaten = 1 * 6 + 4  # Frank eats 1 cookie per day for 6 days and Ted eats 4 cookies on the 6th day

    # Calculate the number of cookies left
    cookies_left = total_cookies - total_cookies_eaten
    result = cookies_left
    return result

print(solution())