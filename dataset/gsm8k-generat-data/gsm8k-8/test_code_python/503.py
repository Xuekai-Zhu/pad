def solution():
    # Calculate the total number of pages
    total_pages = 180 + 100

    # Calculate the number of days Yasna has to read both books
    num_days = 14

    # Calculate the number of pages Yasna needs to read each day
    pages_per_day = total_pages / num_days
    result = pages_per_day
    return result

print(solution())