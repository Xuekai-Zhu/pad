def solution():
    # Find the number of pages Nico read on Wednesday
    total_pages_read = 51  # total number of pages read from Monday to Wednesday
    pages_read_Monday_Tuesday = 20 + 12  # number of pages read on Monday and Tuesday combined
    pages_read_Wednesday = total_pages_read - pages_read_Monday_Tuesday  # number of pages read on Wednesday
    result = pages_read_Wednesday
    return result

print(solution())