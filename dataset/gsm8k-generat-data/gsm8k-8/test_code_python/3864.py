def solution():
    # Define the number of cookies Neil baked
    total_cookies = 20

    # Calculate the number of cookies Neil gave to his friend
    friend_cookies = 2/5 * total_cookies

    # Calculate the number of cookies left for Neil
    left_cookies = total_cookies - friend_cookies
    result = left_cookies
    return result

print(solution())