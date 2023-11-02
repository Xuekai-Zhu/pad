def solution():
    chips_per_bag = 81
    chips_per_cookie = 9
    batches = 3

    # Calculate the total number of chocolate chips in the whole dough
    total_chips = batches * chips_per_bag

    # Calculate the number of cookies that can be made with the total number of chips
    total_cookies = total_chips / chips_per_cookie

    # Calculate the number of cookies in a single batch
    cookies_per_batch = total_cookies / batches
    result = cookies_per_batch
    return result

print(solution())