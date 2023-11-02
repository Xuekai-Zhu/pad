def solution():
    """An air conditioner running for eight hours would consume 7.2 kilowatts. How many kilowatts would the air conditioner consume if it was used for 6 hours a day for 5 days?"""
    hours_per_day = 6
    days = 5
    total_hours = hours_per_day * days
    kilowatts_per_hour = 7.2 / 8
    total_kilowatts = total_hours * kilowatts_per_hour
    result = total_kilowatts
    return result

print(solution())