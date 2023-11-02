def solution():
    # Calculate the number of pages Judy read in the first week
    pages_week1 = 15 * 7  # Judy read for 15 minutes each night, 7 days in the first week

    # Calculate the number of pages Judy read in the second week
    pages_week2 = 100 - pages_week1  # Judy read a total of 100 pages in the second week

    # Calculate the total number of pages Judy read in two weeks
    pages_two_weeks = pages_week2 * 2  # Judy can read 2 pages per 1.5 minutes

    result = pages_two_weeks
    return result

print(solution())