def solution():
    num_half_gallons_per_40_cookies = 10
    num_cookies_per_dozen = 12
    num_dozen_cookies = 200

    # Calculate the total number of cookies needed
    num_cookies = num_dozen_cookies * num_cookies_per_dozen

    # Calculate the total number of half-gallons of milk needed
    num_half_gallons = num_cookies // 40 * num_half_gallons_per_40_cookies

    result = num_half_gallons
    return result

print(solution())