def solution():
    pages_to_read = 30
    percentage_to_read = 0.7  # 70%

    # Calculate the number of pages to read before taking a break
    pages_before_break = pages_to_read * percentage_to_read

    # Calculate the number of pages left to read after taking a break
    pages_after_break = pages_to_read - pages_before_break
    result = pages_after_break
    return result

print(solution())