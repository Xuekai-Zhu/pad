def solution():
    
    total_cookies = 30
    father_cookies = 10
    mother_cookies = father_cookies / 2
    brother_cookies = mother_cookies + 2
    eaten_cookies = father_cookies + mother_cookies + brother_cookies
    left_cookies = total_cookies - eaten_cookies
    result = left_cookies
    return result

print(solution())