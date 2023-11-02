def solution():
    """Katarina has 5 less cookies than Max has. Max has 12 more cookies than the Cookie Monster, and Summer has 23 more cookies than Max. If Katarina has 68 cookies, how many cookies do they have in total?"""
    katarina_cookies = 68
    max_cookies = katarina_cookies + 5
    cookie_monster_cookies = max_cookies - 12
    summer_cookies = max_cookies + 23
    total_cookies = katarina_cookies + max_cookies + cookie_monster_cookies + summer_cookies
    result = total_cookies
    return result

print(solution())