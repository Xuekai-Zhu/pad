def solution():
    cookies_start = 2 + 1  # Kristy ate 2 cookies and gave 1 to her brother
    cookies_friends = 3 + 5 + 5  # Kristy's first friend took 3 cookies, while the next two friends took 5 each
    cookies_end = 6  # There are 6 cookies left

    # Calculate the total number of cookies baked by Kristy
    total_cookies = cookies_start + cookies_friends + cookies_end
    result = total_cookies
    return result

print(solution())