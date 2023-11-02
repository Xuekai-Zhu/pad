def solution():
    # Calculate the total number of chocolate chips needed for one batch of cookies
    chips_per_batch = 81  # a bag of chocolate chips has 81 chips
    chips_per_cookie = 9  # each cookie has 9 chocolate chips
    chips_per_batch_of_cookies = chips_per_batch / 3  # the dough makes three batches of cookies
    cookies_per_batch = chips_per_batch_of_cookies / chips_per_cookie  # calculate the number of cookies per batch

    result = cookies_per_batch
    return result

print(solution())