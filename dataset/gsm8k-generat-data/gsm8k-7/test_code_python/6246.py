def solution():
    total_cookies = 600
    nicole_cookies = (2/5) * total_cookies
    remaining_cookies = total_cookies - nicole_cookies
    eduardo_cookies = (3/5) * remaining_cookies
    remaining_percentage = (remaining_cookies / total_cookies) * 100
    result = remaining_percentage
    return result

print(solution())