def solution():
    # Calculate the total number of chocolate chips used in three batches
    total_chips_used = 81 * 3

    # Calculate the number of cookies made with the total number of chips
    cookies_per_batch = total_chips_used // 9

    result = cookies_per_batch
    return result

print(solution())