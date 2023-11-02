def solution():
    """Jenny buys 1 bag of cookies a week. The bag has 36 cookies and she puts 4 cookies in her son's lunch box 5 days a week. Her husband eats 1 cookie a day for 7 days. Jenny eats the rest of the cookies. How many cookies does Jenny eat?"""
    cookies_per_bag = 36
    cookies_for_son = 4 * 5
    cookies_for_husband = 1 * 7
    cookies_for_jenny = cookies_per_bag - cookies_for_son - cookies_for_husband
    result = cookies_for_jenny
    return result

print(solution())