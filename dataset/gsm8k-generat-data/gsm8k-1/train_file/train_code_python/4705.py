def solution():
    """Harry uses a whole bag of chocolate chips when he makes dough for chocolate chip cookies. The dough makes three batches of cookies, and each cookie has nine chocolate chips in it. A bag of chocolate chips has 81 chips in it. How many cookies are in a batch?"""
    chips_per_bag = 81
    chips_per_cookie = 9
    cookies_per_batch = chips_per_bag // (chips_per_cookie * 3)
    result = cookies_per_batch
    return result

print(solution())