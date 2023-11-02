def solution():
    
    total_cookies = 50
    kept_cookies = 10
    grandparents_cookies = 8
    remaining_cookies = total_cookies - kept_cookies - grandparents_cookies
    class_size = 16
    cookies_per_person = remaining_cookies / class_size
    result = cookies_per_person
    return result

print(solution())