def solution():
    # Calculate the total number of cookies distributed to neighbors
    total_cookies_distributed = 15 * 10

    # Calculate the number of cookies left after all neighbors took their share
    cookies_left = 150 - total_cookies_distributed

    # Calculate the number of cookies Sarah should have taken
    correct_cookies = 10 * 14

    # Calculate the number of cookies Sarah took
    sarah_cookies = correct_cookies - cookies_left

    result = sarah_cookies
    return result

print(solution())