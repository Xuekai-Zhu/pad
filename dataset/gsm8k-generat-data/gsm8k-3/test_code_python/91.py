def solution():
    """John works a job that offers performance bonuses. He makes $80 a day and works for 8 hours. He has the option of working hard to earn the performance bonus of an extra $20 a day, but the extra effort results in a 2-hour longer workday. How much does John make per hour if he decides to earn the bonus?"""
    # Define the base pay and hours worked
    base_pay = 80
    base_hours = 8

    # Define the bonus pay and additional hours worked
    bonus_pay = 20
    bonus_hours = 10

    # Calculate the hourly rate with the base pay
    base_hourly_rate = base_pay / base_hours

    # Calculate the hourly rate with the bonus pay
    bonus_hourly_rate = (base_pay + bonus_pay) / (base_hours + bonus_hours)

    # Choose the higher hourly rate
    if base_hourly_rate > bonus_hourly_rate:
        hourly_rate = base_hourly_rate
    else:
        hourly_rate = bonus_hourly_rate

    result = hourly_rate
    return result

print(solution())