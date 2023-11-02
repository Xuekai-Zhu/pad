def solution():
    janet_daily_pages = 80
    belinda_daily_pages = 30
    weeks = 6

    # Calculate the total number of pages read by each person in 6 weeks
    janet_pages = janet_daily_pages * 7 * weeks
    belinda_pages = belinda_daily_pages * 7 * weeks

    # Calculate the difference in the number of pages read by each person in 6 weeks
    pages_difference = janet_pages - belinda_pages
    result = pages_difference
    return result

print(solution())