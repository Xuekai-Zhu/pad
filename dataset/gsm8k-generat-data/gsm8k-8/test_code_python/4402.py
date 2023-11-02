def solution():
    # Calculate the number of cookies baked on Tuesday
    tues_cookies = 32 / 2

    # Calculate the number of cookies baked on Wednesday
    wed_cookies = 3 * tues_cookies - 4

    # Calculate the total number of cookies baked
    total_cookies = 32 + tues_cookies + wed_cookies

    result = total_cookies
    return result

print(solution())