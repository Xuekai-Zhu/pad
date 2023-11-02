def solution():
    """Maria has 19 cookies. She decided to give her friend 5 of them, and half of the rest to her family. 
    From the rest, Maria decided to eat 2 cookies. How many cookies will she have left?"""
    initial_cookies = 19
    friend_cookies = 5
    remaining_cookies = initial_cookies - friend_cookies
    family_cookies = remaining_cookies / 2
    remaining_cookies -= family_cookies
    remaining_cookies -= 2  # Maria eats 2 cookies
    result = remaining_cookies
    return result

print(solution())