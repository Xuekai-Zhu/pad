def solution():
    
    total_cookies = 50
    cookies_kept = 10
    cookies_given = 8
    cookies_left = total_cookies - (cookies_kept + cookies_given)
    cookies_per_person = cookies_left // 16
    result = cookies_per_person
    return result

print(solution())