def solution():
    """Uncle Jude baked 256 cookies. He gave 15 cookies to Tim, 23 cookies to Mike, kept some in the fridge and gave the rest to Anna. How many cookies did he put in the fridge if he gave twice as many cookies as he gave Tim to Anna?"""
    total_cookies = 256
    cookies_given_tim = 15
    cookies_given_mike = 23
    cookies_given_others = cookies_given_tim + cookies_given_mike
    cookies_remaining = total_cookies - cookies_given_others
    cookies_given_anna = cookies_given_tim * 2
    cookies_in_fridge = cookies_remaining - cookies_given_anna
    result = cookies_in_fridge
    
    return result

print(solution())