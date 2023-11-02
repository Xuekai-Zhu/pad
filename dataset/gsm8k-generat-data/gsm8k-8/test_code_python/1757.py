def solution():
    # Calculate the total number of pages Arthur has already read
    pages_read = 0.8 * 500 + 0.2 * 1000
    # Calculate the number of pages Arthur still needs to read
    pages_remaining = 800 - pages_read
    result = pages_remaining
    return result

print(solution())