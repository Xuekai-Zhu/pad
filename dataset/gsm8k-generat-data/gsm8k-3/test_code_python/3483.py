def solution():
    """Mark collects money for the homeless.  He visits 20 households a day for 5 days and half of those households give him a pair of 20s.  How much did he collect?"""
    # Define the number of households visited per day and the number of days
    HOUSEHOLDS_PER_DAY = 20
    DAYS = 5

    # Calculate the number of households visited over the 5 days
    total_households = HOUSEHOLDS_PER_DAY * DAYS

    # Calculate the number of households that gave Mark a pair of 20s
    pairs_of_20s = total_households // 2

    # Calculate the total amount collected
    total_collected = pairs_of_20s * 40

    # Display the total amount collected
    result = total_collected
    return result

print(solution())