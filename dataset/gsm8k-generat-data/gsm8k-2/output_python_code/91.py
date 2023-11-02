def solution():
    """John works a job that offers performance bonuses. He makes $80 a day and works for 8 hours. He has the option of working hard to earn the performance bonus of an extra $20 a day, but the extra effort results in a 2-hour longer workday. How much does John make per hour if he decides to earn the bonus?"""
    normal_pay = 80
    bonus_pay = 100  # (80 + 20)
    normal_hours = 8
    bonus_hours = 10  # (8 + 2)
    normal_pay_per_hour = normal_pay / normal_hours
    bonus_pay_per_hour = bonus_pay / bonus_hours
    result = bonus_pay_per_hour
    return result

print(solution())