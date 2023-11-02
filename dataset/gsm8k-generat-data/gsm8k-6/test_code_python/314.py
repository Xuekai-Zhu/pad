def solution():
    # Calculate the total number of pages read from Sunday to Friday
    total_pages = 43 + 65 + 28 + 0 + 70 + 56

    # Calculate how many pages Berry needs to read on Saturday to reach his goal
    remaining_pages = (7 * 50) - total_pages

    result = remaining_pages
    return result

print(solution())