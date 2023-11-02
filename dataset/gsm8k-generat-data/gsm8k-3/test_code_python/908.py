def solution():
    """John runs a telethon to raise money.  For the first 12 hours, he generates $5000 per hour.  The remaining 14 hours, he generates 20% more per hour.  How much total money does he make?"""
    # Calculate the total money generated in the first 12 hours
    money_12_hours = 12 * 5000

    # Calculate the increase in money generated per hour for the remaining 14 hours
    increase = 0.2 * 5000

    # Calculate the money generated per hour for the remaining 14 hours
    money_hourly = 5000 + increase

    # Calculate the total money generated for the remaining 14 hours
    money_14_hours = 14 * money_hourly

    # Calculate the total money generated
    total_money = money_12_hours + money_14_hours

    # Display the total money generated
    result = total_money
    return result

print(solution())