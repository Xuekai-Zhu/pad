def solution():
    
    total_cookies = 30
    father_cookies = 10
    mother_cookies = father_cookies / 2
    brother_cookies = mother_cookies + 2
    remaining_cookies = total_cookies - father_cookies - mother_cookies - brother_cookies
    result = remaining_cookies
    return result

print(solution())