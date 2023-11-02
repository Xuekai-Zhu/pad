def solution():
    
    cookies = 19
    cookies -= 5  
    family_cookies = cookies // 2
    cookies -= family_cookies  
    cookies -= 2  
    result = cookies
    return result

print(solution())