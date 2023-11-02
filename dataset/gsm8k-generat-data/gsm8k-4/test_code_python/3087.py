def solution():
    """While planning to finish reading a 140-page book in one week, Jessy initially decides to read 3 times daily, 6 pages each time, every day of the week. How many more pages should she read per day to actually achieve her goal?"""
    # Calculate the total number of pages Jessy planned to read in a week
    planned_pages = 3 * 6 * 7

    # Calculate the number of additional pages Jessy needs to read to achieve her goal
    additional_pages = 140 - planned_pages

    # Calculate the number of additional pages Jessy needs to read per day to achieve her goal
    additional_pages_per_day = additional_pages / 7

    # return the result
    result = additional_pages_per_day
    return result

print(solution())