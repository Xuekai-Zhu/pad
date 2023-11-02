def solution():
    """Kristy baked cookies because her friends are coming over to her house. She ate 2 of them and gave her brother 1 cookie. Her first friend arrived and took 3 cookies. The second and third friends to arrive took 5 cookies each. If there are 6 cookies left, how many cookies did Kristy bake?"""
    cookies_eaten = 2
    cookies_given = 1
    cookies_taken = 3 + 5 + 5
    cookies_left = 6
    total_cookies = cookies_eaten + cookies_given + cookies_taken + cookies_left
    result = total_cookies
    return result

print(solution())