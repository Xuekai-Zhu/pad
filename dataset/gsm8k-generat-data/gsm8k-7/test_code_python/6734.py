def solution():
    total_cookies = 120

    # Calculate the number of cookies sold in the morning
    morning_cookies = 3 * 12

    # Calculate the total number of cookies sold during the day
    total_sold = morning_cookies + 57 + 16

    # Calculate the number of cookies left to take home
    remaining_cookies = total_cookies - total_sold
    result = remaining_cookies
    return result

print(solution())