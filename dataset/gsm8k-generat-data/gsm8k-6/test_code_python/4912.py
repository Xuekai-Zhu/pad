def solution():
    # Calculate the number of pages Joey will read before taking a break
    pages_before_break = 0.7 * 30  # Joey will take a break after reading 70% of the pages assigned
    # Calculate the number of pages Joey will have left to read after taking a break
    pages_after_break = 30 - pages_before_break
    result = pages_after_break
    return result

print(solution())