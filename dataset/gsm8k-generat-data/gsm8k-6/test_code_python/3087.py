def solution():
    # Calculate the initial number of pages Jessy planned to read
    initial_pages = 3 * 6 * 7  # Jessy planned to read 3 times daily, 6 pages each time, every day of the week

    # Calculate how many more pages Jessy needs to read each day to achieve her goal
    remaining_pages = 140 - initial_pages
    days_left = 7
    more_pages_per_day = remaining_pages / days_left / 3
    result = more_pages_per_day
    return result

print(solution())