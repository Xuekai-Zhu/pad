def solution():
    """Harry uses a whole bag of chocolate chips when he makes dough for chocolate chip cookies. The dough makes three batches of cookies, and each cookie has nine chocolate chips in it. A bag of chocolate chips has 81 chips in it. How many cookies are in a batch?"""
    # Define the number of chocolate chips per bag
    CHOCOLATE_CHIPS_PER_BAG = 81

    # Calculate the number of chocolate chips per cookie
    CHOCOLATE_CHIPS_PER_COOKIE = CHOCOLATE_CHIPS_PER_BAG / 3 / 9

    # Calculate the number of cookies per batch
    COOKIES_PER_BATCH = 1 / CHOCOLATE_CHIPS_PER_COOKIE

    # Display the number of cookies per batch
    result = COOKIES_PER_BATCH
    return result

print(solution())