def solution():
    
    total_cookies = 60
    nut_cookies = int(total_cookies * 0.25)
    choc_cookies = int(total_cookies * 0.4)
    nut_and_choc_cookies = total_cookies - nut_cookies - choc_cookies
    total_nuts = (nut_cookies + nut_and_choc_cookies) * 2
    result = total_nuts
    return result

print(solution())