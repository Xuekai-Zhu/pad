def solution():
    
    total_cookies = 600
    nicole_cookies = total_cookies * 2/5
    remaining_cookies = total_cookies - nicole_cookies
    eduardo_cookies = remaining_cookies * 3/5
    remaining_percentage = (remaining_cookies - eduardo_cookies) / total_cookies * 100
    result = remaining_percentage
    return result

print(solution())