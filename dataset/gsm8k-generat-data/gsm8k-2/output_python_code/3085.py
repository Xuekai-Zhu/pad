def solution():
    """A retail store wants to hire 50 new phone reps to assist with the increased call volume that they will experience over the holiday. Each phone rep will work 8 hours a day and will be paid $14.00 an hour. After 5 days, how much will the company pay all 50 new employees?"""
    num_reps = 50
    hours_per_day = 8
    hourly_rate = 14
    days_worked = 5
    total_hours = num_reps * hours_per_day * days_worked
    total_pay = total_hours * hourly_rate
    result = total_pay
    return result

print(solution())