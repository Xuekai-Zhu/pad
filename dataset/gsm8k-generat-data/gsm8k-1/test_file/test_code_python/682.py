def solution():
    """Greta and Celinda are baking cookies. Greta bakes 30 cookies and Celinda bakes twice as many. If the pair eat 10 of the cookies while they are cooling and put the rest in a box, how many cookies are there in the box?"""
    greta_cookies = 30
    celinda_cookies = greta_cookies * 2
    total_cookies = greta_cookies + celinda_cookies - 10
    result = total_cookies
    return result

print(solution())