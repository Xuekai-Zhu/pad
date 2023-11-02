def solution():
    """Maria has 19 cookies. She decided to give her friend 5 of them, and half of the rest to her family. From the rest, Maria decided to eat 2 cookies. How many cookies will she have left?"""
    cookies = 19
    cookies -= 5  # Giving 5 to a friend
    family_cookies = cookies // 2
    cookies -= family_cookies  # Giving half to family
    cookies -= 2  # Eating 2 herself
    result = cookies
    return result

print(solution())