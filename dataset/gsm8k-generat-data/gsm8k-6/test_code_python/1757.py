def solution():
    # Calculate the total number of pages Arthur has read
    pages_read = 500 * 0.8 + 1000/5  

    # Calculate the number of pages he still needs to read to meet his goal
    pages_remaining = 800 - pages_read
    result = pages_remaining
    return result

print(solution())