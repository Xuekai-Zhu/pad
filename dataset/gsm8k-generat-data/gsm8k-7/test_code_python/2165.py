def solution():
    total_pages = 381
    pages_read = 149
    pages_per_day = 20
    days = 7

    # Calculate the total pages read during the week
    pages_read_week = pages_per_day * days

    # Calculate the total pages left to be read
    pages_left = total_pages - pages_read - pages_read_week
    result = pages_left
    return result

print(solution())