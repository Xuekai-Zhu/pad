def solution():
    """Mark is injured so decides to spend more time reading.  He used to read 2 hours a day but increased that by 150%.  Before he read 100 pages a day.  How many pages does he read a week now?"""
    # Define Mark's previous reading habits
    previous_reading_hours = 2
    previous_reading_pages = 100

    # Calculate Mark's new reading time
    new_reading_hours = previous_reading_hours * (1 + 1.5)
    # There are 7 days in a week, so multiply by 7 to get weekly reading time
    new_weekly_reading_hours = new_reading_hours * 7

    # Calculate Mark's new reading speed
    new_reading_speed = previous_reading_pages / previous_reading_hours

    # Calculate Mark's new weekly reading total
    new_weekly_reading_pages = new_reading_speed * new_weekly_reading_hours
    result = new_weekly_reading_pages
    return result

print(solution())