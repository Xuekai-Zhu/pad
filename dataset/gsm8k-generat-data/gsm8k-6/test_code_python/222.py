def solution():
    # Calculate the total number of pages Bekah still needs to read
    pages_left = 408 - 113  # she already read 113 pages over the weekend

    # Calculate the number of pages Bekah needs to read each day for the next 5 days to complete her assignment
    pages_per_day = pages_left / 5

    result = pages_per_day
    return result

print(solution())