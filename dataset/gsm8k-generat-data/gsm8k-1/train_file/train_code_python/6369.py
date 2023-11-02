def solution():
    """A mechanic charges $60 an hour to repair a car. He works 8 hours a day for 14 days on one car. The mechanic also used $2500 in parts. How much did the car's owner have to pay?"""
    hourly_rate = 60
    hours_per_day = 8
    days_worked = 14
    total_hours = hours_per_day * days_worked
    labor_cost = total_hours * hourly_rate
    parts_cost = 2500
    total_cost = labor_cost + parts_cost
    result = total_cost
    return result

print(solution())