def solution():
    pounds_of_butter_per_batch = 4
    batches = 1
    cookies_per_pound = 48
    cookies_needed = 4 * 12
    pounds_needed = (cookies_needed / cookies_per_pound) / batches
    result = pounds_needed
    return result

print(solution())