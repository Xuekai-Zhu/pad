def solution():
    total_cookies = 600
    cookies_eaten_nicole = 2/5 * total_cookies
    cookies_eaten_eduardo = 3/5 * (total_cookies - cookies_eaten_nicole)
    cookies_remaining = total_cookies - cookies_eaten_nicole - cookies_eaten_eduardo
    percent_cookies_remaining = cookies_remaining / total_cookies * 100
    result = percent_cookies_remaining
    
    return result

print(solution())