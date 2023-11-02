def solution():
    """The sewers in Middleton can handle 240,000 gallons of run-off. Each hour of rain produces 1000 gallons of runoff. How many days of rain can the sewers handle before they overflow?"""
    # Define the sewer capacity and the amount of runoff produced each hour
    SEWER_CAPACITY = 240000
    RUNOFF_PER_HOUR = 1000

    # Calculate the amount of runoff produced each day
    RUNOFF_PER_DAY = RUNOFF_PER_HOUR * 24

    # Calculate the number of days before the sewer overflows
    days_before_overflow = SEWER_CAPACITY / RUNOFF_PER_DAY

    result = days_before_overflow
    return result

print(solution())