def solution():
    # Calculate the number of pages Sammy uses for his science project
    science_pages = 0.25 * 120

    # Calculate the total number of pages Sammy uses
    total_pages_used = science_pages + 10

    # Calculate the number of pages remaining in the pad
    pages_remaining = 120 - total_pages_used

    result = pages_remaining
    return result

print(solution())