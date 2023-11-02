def solution():
    """Mark is injured so decides to spend more time reading. He used to read 2 hours a day but increased that by 150%. Before he read 100 pages a day. How many pages does he read a week now?"""
    # Define the initial number of hours read and the increase percentage
    INITIAL_HOURS_READ = 2
    INCREASE_PERCENTAGE = 150

    # Define the initial number of pages read per day
    INITIAL_PAGES_READ_PER_DAY = 100

    # Calculate the new number of hours read per day
    new_hours_read_per_day = INITIAL_HOURS_READ * (1 + INCREASE_PERCENTAGE/100)

    # Calculate the new number of pages read per day
    new_pages_read_per_day = INITIAL_PAGES_READ_PER_DAY * (new_hours_read_per_day / INITIAL_HOURS_READ)

    # Calculate the total number of pages read per week
    pages_read_per_week = new_pages_read_per_day * 7

    result = pages_read_per_week
    return result

print(solution())