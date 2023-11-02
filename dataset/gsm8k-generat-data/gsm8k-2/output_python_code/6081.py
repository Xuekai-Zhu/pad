def solution():
    """Chris has half as many cookies as Kenny. Glenn has four times as many cookies as Kenny. How many cookies do these three boys have, if Glenn has 24 cookies?"""
    glenn_cookies = 24
    kenny_cookies = glenn_cookies / 4
    chris_cookies = kenny_cookies / 2
    total_cookies = glenn_cookies + kenny_cookies + chris_cookies
    result = total_cookies
    return result

print(solution())