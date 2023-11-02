def solution():
    morning_butter_cookies = 20
    morning_biscuits = 40
    afternoon_butter_cookies = 10
    afternoon_biscuits = 20

    # Calculate the total number of butter cookies baked
    total_butter_cookies = morning_butter_cookies + afternoon_butter_cookies

    # Calculate the total number of biscuits baked
    total_biscuits = morning_biscuits + afternoon_biscuits

    # Calculate the difference between the number of biscuits and butter cookies
    difference = total_biscuits - total_butter_cookies
    result = difference
    return result

print(solution())