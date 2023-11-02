def solution():
    pages_per_day = 2 * 50  # John reads 2 hours a day at a rate of 50 pages an hour
    total_pages = 2800  # The bible is 2800 pages long

    # Calculate the number of days John will take to read the bible
    total_days = total_pages / pages_per_day

    # Convert total days to weeks
    total_weeks = total_days / 7
    result = total_weeks
    return result

print(solution())