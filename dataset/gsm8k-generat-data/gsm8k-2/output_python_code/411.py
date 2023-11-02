def solution():
    """Uncle Jude baked 256 cookies. He gave 15 cookies to Tim, 23 cookies to Mike, kept some in the fridge and gave the rest to Anna. How many cookies did he put in the fridge if he gave twice as many cookies as he gave Tim to Anna?"""
    total_cookies = 256
    tim_cookies = 15
    mike_cookies = 23
    anna_cookies = total_cookies - tim_cookies - mike_cookies
    tim_to_anna_cookies = 2 * tim_cookies
    cookies_in_fridge = anna_cookies - tim_to_anna_cookies
    result = cookies_in_fridge
    return result

print(solution())