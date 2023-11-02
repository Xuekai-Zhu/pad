def solution():
    pages_read_Monday = 23
    pages_read_Tuesday = 38
    pages_read_Wednesday = 61
    total_pages_read = pages_read_Monday + pages_read_Tuesday + pages_read_Wednesday
    pages_left_to_read = 158 - total_pages_read
    pages_to_read_Thursday = pages_left_to_read / 2
    result = pages_to_read_Thursday
    return result

print(solution())