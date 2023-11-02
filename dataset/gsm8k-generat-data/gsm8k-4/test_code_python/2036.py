def solution():
    """Mr. Johnson has a prescription with enough pills for 30 days. After four-fifths of the days, he has 12 pills left. How many pills is Mr. Johnson supposed to take a day if he takes the same dose daily?"""
    # Define the number of days Mr. Johnson has taken pills
    days_taken = 30 * (4/5)

    # Define the number of pills Mr. Johnson has taken so far
    pills_taken = 30*1 - 12

    # Calculate the average number of pills Mr. Johnson takes per day
    pills_per_day = pills_taken / days_taken

    # Return the result
    result = pills_per_day
    return result

print(solution())