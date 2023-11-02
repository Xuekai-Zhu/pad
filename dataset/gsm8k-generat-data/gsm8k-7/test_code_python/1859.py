def solution():
    janet_pages_per_day = 80
    belinda_pages_per_day = 30
    num_weeks = 6

    # Calculate the total number of pages Janet reads in 6 weeks
    janet_total_pages = janet_pages_per_day * 7 * num_weeks

    # Calculate the total number of pages Belinda reads in 6 weeks
    belinda_total_pages = belinda_pages_per_day * 7 * num_weeks

    # Calculate the difference in pages read between Janet and Belinda
    diff = janet_total_pages - belinda_total_pages
    result = diff
    return result

print(solution())