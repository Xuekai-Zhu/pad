def solution():
    """John works a job that offers performance bonuses. He makes $80 a day and works for 8 hours. He has the option of working hard to earn the performance bonus of an extra $20 a day, but the extra effort results in a 2-hour longer workday. How much does John make per hour if he decides to earn the bonus?"""
    regular_pay = 80
    bonus_pay = 100
    regular_hours = 8
    bonus_hours = 10
    hourly_rate = regular_pay / regular_hours
    bonus_hourly_rate = bonus_pay / bonus_hours
    result = bonus_hourly_rate
    
    return result

print(solution())