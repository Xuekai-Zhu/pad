def solution():
    
    monday_cookies = 32
    tuesday_cookies = monday_cookies / 2
    wednesday_cookies = tuesday_cookies * 3 - 4
    total_cookies = monday_cookies + tuesday_cookies + wednesday_cookies
    result = total_cookies
    return result

print(solution())