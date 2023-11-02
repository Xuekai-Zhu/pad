def solution():
    
    
    
    total_cookies = 200
    
    
    wife_cookies = int(total_cookies * 0.3)
    
    
    remaining_cookies = total_cookies - wife_cookies
    
    
    daughter_cookies = 40
    
    
    remaining_cookies -= daughter_cookies
    
    
    javier_cookies = int(remaining_cookies / 2)
    
    
    not_eaten_cookies = remaining_cookies - javier_cookies
    
    return not_eaten_cookies

print(solution())