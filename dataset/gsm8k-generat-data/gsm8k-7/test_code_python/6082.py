def solution():
    glenn_cookies = 24
    kenny_cookies = glenn_cookies / 4  # Kenny has 4 times fewer cookies than Glenn
    chris_cookies = kenny_cookies / 2  # Chris has half as many cookies as Kenny
    total_cookies = glenn_cookies + kenny_cookies + chris_cookies
    result = total_cookies
    return result

print(solution())