def solution():
    
    total_cookies = 55
    eaten_cookies = 5
    remaining_cookies = total_cookies - eaten_cookies
    jars = 5
    cookies_per_jar = remaining_cookies / jars
    result = cookies_per_jar
    return result

print(solution())