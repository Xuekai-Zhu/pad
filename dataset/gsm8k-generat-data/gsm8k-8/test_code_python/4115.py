def solution():
    # Calculate the total number of cookies needed
    total_cookies = 24 * 10

    # Calculate the number of cookies per batch
    cookies_per_batch = 4 * 12

    # Calculate the total number of cookies made so far
    total_cookies_made = (2 * cookies_per_batch) + cookies_per_batch

    # Calculate the number of batches needed to make the remaining cookies
    batches_needed = (total_cookies - total_cookies_made) / cookies_per_batch

    result = batches_needed
    return result

print(solution())