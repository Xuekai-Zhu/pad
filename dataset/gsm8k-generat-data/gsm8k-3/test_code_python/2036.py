def solution():
    """Mr. Johnson has a prescription with enough pills for 30 days. After four-fifths of the days, he has 12 pills left. How many pills is Mr. Johnson supposed to take a day if he takes the same dose daily?"""

    # Define variables
    total_days = 30
    remaining_days = total_days - (total_days * 4/5)
    remaining_pills = 12

    # Calculate the number of pills taken per day
    pills_per_day = remaining_pills / remaining_days

    # Round up to the nearest whole pill
    pills_per_day = round(pills_per_day)

    # Display the number of pills per day
    result = pills_per_day
    return result

print(solution())