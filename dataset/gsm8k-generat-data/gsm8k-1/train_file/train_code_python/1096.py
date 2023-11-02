def solution():
    """Out of the 200 cookies that Javier baked from the recipe he learned online, his wife took 30%, and his daughter took 40 from the remaining cookies. If he ate half of the remaining cookies, how many cookies did they not eat?"""
    
    # Total cookies baked
    total_cookies = 200
    
    # Cookies taken by wife
    wife_cookies = int(total_cookies * 0.3)
    
    # Cookies remaining after wife
    remaining_cookies = total_cookies - wife_cookies
    
    # Cookies taken by daughter
    daughter_cookies = 40
    
    # Cookies remaining after daughter
    remaining_cookies -= daughter_cookies
    
    # Cookies eaten by Javier
    javier_cookies = int(remaining_cookies / 2)
    
    # Cookies not eaten
    not_eaten_cookies = remaining_cookies - javier_cookies
    
    return not_eaten_cookies

print(solution())