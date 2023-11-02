def solution():
    """John buys 2 dozen cookies. He eats 3. How many cookies does he have left?"""
    # Define the initial number of cookies
    initial_cookies = 2 * 12

    # Define the number of cookies he eats
    cookies_eaten = 3

    # Calculate the number of cookies he has left
    cookies_left = initial_cookies - cookies_eaten

    # return the result
    result = cookies_left
    return result

print(solution())