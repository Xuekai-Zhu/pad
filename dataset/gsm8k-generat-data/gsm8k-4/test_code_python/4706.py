def solution():
    """Harry uses a whole bag of chocolate chips when he makes dough for chocolate chip cookies. The dough makes three batches of cookies, and each cookie has nine chocolate chips in it. A bag of chocolate chips has 81 chips in it. How many cookies are in a batch?"""
    # Define the number of chocolate chips in a bag
    CHIPS_PER_BAG = 81

    # Calculate the total number of chocolate chips used for the dough
    chips_used = CHIPS_PER_BAG

    # Calculate the number of chocolate chips in each cookie
    chips_per_cookie = 9

    # Calculate the total number of cookies that can be made with the dough
    total_cookies = chips_used // chips_per_cookie

    # Calculate the number of cookies in a batch
    cookies_per_batch = total_cookies // 3

    # Return the result
    result = cookies_per_batch
    return result

print(solution())