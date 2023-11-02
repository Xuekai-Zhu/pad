def solution():
    """An air conditioner running for eight hours would consume 7.2 kilowatts. How many kilowatts would the air conditioner consume if it was used for 6 hours a day for 5 days?"""
    # Define the kilowatts consumed per hour
    kw_per_hour = 7.2 / 8

    # Calculate the total kilowatts consumed over 5 days of 6 hours each
    total_hours = 6 * 5
    total_kw = kw_per_hour * total_hours

    # return the result
    result = total_kw
    return result

print(solution())