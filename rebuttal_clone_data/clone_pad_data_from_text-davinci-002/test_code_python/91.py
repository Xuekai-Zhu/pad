def solution():
    """John works a job that offers performance bonuses. He makes $80 a day and works for 8 hours. He has the option of working hard to earn the performance bonus of an extra $20 a day, but the extra effort results in a 2-hour longer workday. How much does John make per hour if he decides to earn the bonus?"""
    base_pay_per_day = 80
    bonus_pay_per_day = 20
    extra_hours_worked = 2
    total_hours_worked = 8 + extra_hours_worked
    total_pay_per_day = base_pay_per_day + bonus_pay_per_day
    total_pay_per_hour = total_pay_per_day / total_hours_worked
    result = total_pay_per_hour
    
    return result

print(solution())