def solution():
    """Lani baked 55 cookies. She ate 5 five cookies and placed the rest equally into five jars. How many cookies were in each jar?"""
    total_cookies = 55
    eaten_cookies = 5
    num_jars = 5
    cookies_per_jar = (total_cookies - eaten_cookies) / num_jars
    result = cookies_per_jar
    return result

print(solution())