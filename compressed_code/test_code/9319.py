def solution():
    
    monday_cookies = 5
    tuesday_cookies = 2 * monday_cookies
    wednesday_cookies = tuesday_cookies * 1.4
    total_cookies = monday_cookies + tuesday_cookies + wednesday_cookies
    result = total_cookies
    return result

print(solution())