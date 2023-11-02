def solution():
    # Define the number of days in 6 weeks
    days_in_6_weeks = 6 * 7

    # Calculate the number of pages Janet reads in 6 weeks
    janet_total_pages = 80 * days_in_6_weeks

    # Calculate the number of pages Belinda reads in 6 weeks
    belinda_total_pages = 30 * days_in_6_weeks

    # Calculate the difference in pages read
    difference_pages = janet_total_pages - belinda_total_pages
    result = difference_pages
    return result

print(solution())