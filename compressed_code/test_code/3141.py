def solution():
    
    total_cookies = 120
    num_adults = 2
    num_children = 4
    adult_cookies = total_cookies // 3
    child_cookies = total_cookies - adult_cookies
    cookies_per_child = child_cookies // num_children
    result = cookies_per_child
    return result

print(solution())