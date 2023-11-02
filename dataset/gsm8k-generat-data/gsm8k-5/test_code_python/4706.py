def solution():
    # Calculate the total number of chocolate chips used in the dough
    total_chips = 81

    # Calculate the number of chocolate chips in each cookie
    chips_per_cookie = 9

    # Calculate the total number of cookies in three batches
    cookies_per_batch = total_chips / chips_per_cookie
    total_cookies = cookies_per_batch * 3
    result = total_cookies
    return result

print(solution())