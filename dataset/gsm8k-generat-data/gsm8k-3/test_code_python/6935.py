def solution():
    """An air conditioner running for eight hours would consume 7.2 kilowatts. How many kilowatts would the air conditioner consume if it was used for 6 hours a day for 5 days?"""
    # Define the number of hours and kilowatts consumed per hour
    HOURS_PER_DAY = 6
    DAYS = 5
    KILOWATTS_PER_HOUR = 0.9

    # Calculate the total number of hours the air conditioner is used
    total_hours = HOURS_PER_DAY * DAYS

    # Calculate the total number of kilowatts consumed
    total_kilowatts = total_hours * KILOWATTS_PER_HOUR

    # Display the total kilowatts consumed
    result = total_kilowatts
    return result

print(solution())