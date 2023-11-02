def solution():
    initial_cookies = 19
    friend_cookies = 5
    remaining_cookies = initial_cookies - friend_cookies
    family_cookies = remaining_cookies / 2
    remaining_cookies -= family_cookies
    remaining_cookies -= 2
    result = remaining_cookies
    return result

print(solution())