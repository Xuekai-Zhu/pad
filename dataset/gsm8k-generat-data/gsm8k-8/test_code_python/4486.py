def solution():
    # Define the number of cookies eaten on each day
    monday_cookies = 5
    tuesday_cookies = 2 * monday_cookies
    wednesday_cookies = 1.4 * tuesday_cookies # 40% more than Tuesday

    # Calculate the total number of cookies eaten
    total_cookies = monday_cookies + tuesday_cookies + wednesday_cookies
    result = total_cookies
    return result

print(solution())