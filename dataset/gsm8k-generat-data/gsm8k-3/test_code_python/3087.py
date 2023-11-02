def solution():
    """While planning to finish reading a 140-page book in one week, Jessy initially decides to read 3 times daily, 6 pages each time, every day of the week. How many more pages should she read per day to actually achieve her goal?"""
    # Define the number of pages Jessy initially planned to read per day
    planned_pages_per_day = 3 * 6

    # Define the total number of pages Jessy needs to read
    total_pages = 140

    # Define the total number of days Jessy has to read the book
    total_days = 7

    # Calculate the number of pages Jessy needs to read per day to achieve her goal
    actual_pages_per_day = (total_pages - planned_pages_per_day * total_days) / total_days

    # Display the number of additional pages Jessy needs to read per day to achieve her goal
    result = actual_pages_per_day - planned_pages_per_day
    return result

print(solution())