def solution():
    """John works a job that offers performance bonuses. He makes $80 a day and works for 8 hours. He has the option of working hard to earn the performance bonus of an extra $20 a day, but the extra effort results in a 2-hour longer workday. How much does John make per hour if he decides to earn the bonus?"""
    # Define the base pay and hours worked for John
    base_pay = 80
    base_hours = 8

    # Define the bonus pay and additional hours worked for John
    bonus_pay = 20
    bonus_hours = 10

    # Calculate John's hourly rate with and without the bonus
    hourly_rate_no_bonus = base_pay / base_hours
    hourly_rate_with_bonus = (base_pay + bonus_pay) / bonus_hours

    # Determine if it is worth it for John to work for the bonus
    if hourly_rate_with_bonus > hourly_rate_no_bonus:
        result = hourly_rate_with_bonus
    else:
        result = hourly_rate_no_bonus
    return result

print(solution())