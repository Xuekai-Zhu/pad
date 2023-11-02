def solution():
    # Calculate the total number of pages Arthur has already read
    pages_read = (0.8 * 500) + (0.2 * 1000/5)  # 80% of 500-page book plus 1/5 of a 1000-page book

    # Calculate how many more pages Arthur needs to read to meet his goal
    pages_remaining = 800 - pages_read
    result = pages_remaining
    return result

print(solution())