def solution():
    # Calculate the number of cookies Kenny has
    kenny_cookies = 24 / 4  # Glenn has 4 times as many cookies as Kenny
    # Calculate the number of cookies Chris has
    chris_cookies = kenny_cookies / 2  # Chris has half as many cookies as Kenny
    # Calculate the total number of cookies the three boys have
    total_cookies = kenny_cookies + chris_cookies + 24  # Glenn has 24 cookies
    result = total_cookies
    return result

print(solution())