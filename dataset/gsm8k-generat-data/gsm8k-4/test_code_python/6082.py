def solution():
    """Chris has half as many cookies as Kenny. Glenn has four times as many cookies as Kenny. How many cookies do these three boys have, if Glenn has 24 cookies?"""
    # Define the number of cookies Glenn has
    glenn_cookies = 24

    # Calculate the number of cookies Kenny has
    kenny_cookies = glenn_cookies / 4

    # Calculate the number of cookies Chris has
    chris_cookies = kenny_cookies / 2

    # Calculate the total number of cookies
    total_cookies = glenn_cookies + kenny_cookies + chris_cookies

    # return the result
    result = total_cookies
    return result

print(solution())