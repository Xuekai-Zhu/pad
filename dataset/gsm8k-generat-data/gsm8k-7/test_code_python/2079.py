def solution():
    num_cookies_initial = 0
    num_cookies_initial += 2 # Kristy ate 2 cookies
    num_cookies_initial -= 1 # Kristy gave 1 cookie to her brother
    num_cookies_initial -= 3 # First friend took 3 cookies
    num_cookies_initial -= 5 # Second friend took 5 cookies
    num_cookies_initial -= 5 # Third friend took 5 cookies
    num_cookies_left = 6 

    # Calculate the total number of cookies that Kristy baked
    num_cookies_baked = num_cookies_initial + num_cookies_left
    result = num_cookies_baked
    return result

print(solution())