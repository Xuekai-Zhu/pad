def solution():
    total_pages = 140
    num_days = 7
    initial_pages_per_day = 3 * 6  # 3 times daily, 6 pages each time
    initial_total_pages_read = initial_pages_per_day * num_days

    # Calculate the remaining pages that Jessy needs to read to achieve her goal
    remaining_pages = total_pages - initial_total_pages_read

    # Calculate the additional pages per day that Jessy needs to read to achieve her goal
    additional_pages_per_day = remaining_pages / num_days
    result = additional_pages_per_day
    return result

print(solution())