def solution():
    # Calculate the total number of pages Elliot will read in a week
    pages_per_week = 20 * 7

    # Calculate the total number of pages Elliot has left to read
    pages_left = 381 - 149 - pages_per_week
    result = pages_left
    return result

print(solution())