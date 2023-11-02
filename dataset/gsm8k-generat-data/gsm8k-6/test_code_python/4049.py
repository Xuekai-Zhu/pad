def solution():
    # Calculate the total number of pages read by Ethan
    pages_read = 40 + 10 + 2 * (40 + 10)  # twice the total pages as on Saturday

    # Calculate the number of pages left to read
    pages_left = 360 - pages_read
    result = pages_left
    return result

print(solution())