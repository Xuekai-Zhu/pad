def solution():
    """John reads his bible every day.  He reads for 2 hours a day and reads at a rate of 50 pages an hour.  If the bible is 2800 pages long how many weeks will it take him to read it all?"""
    # Define John's reading rate in pages per day
    READ_RATE = 2 * 50

    # Define the total number of pages in the bible
    TOTAL_PAGES = 2800

    # Calculate the number of days it will take John to read the bible
    num_days = TOTAL_PAGES / READ_RATE

    # Calculate the number of weeks it will take John to read the bible
    num_weeks = num_days / 7

    # Display the number of weeks
    result = num_weeks
    return result

print(solution())