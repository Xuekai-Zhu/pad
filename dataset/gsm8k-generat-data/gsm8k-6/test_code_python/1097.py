def solution():
    total_cookies = 200
    wife_cookies = int(total_cookies * 0.3)
    remaining_cookies = total_cookies - wife_cookies
    daughter_cookies = 40
    remaining_cookies -= daughter_cookies
    remaining_cookies /= 2
    result = remaining_cookies
    return result

print(solution())