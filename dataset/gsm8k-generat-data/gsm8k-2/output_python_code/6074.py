def solution():
    """Tim hires two bodyguards. They each charge $20 an hour. He hires them for 8 hour per day. How much does he pay them in a week if he hires them 7 days a week?"""
    hourly_rate = 20
    hours_per_day = 8
    num_of_guards = 2
    num_of_days = 7
    total_pay = hourly_rate * hours_per_day * num_of_guards * num_of_days
    result = total_pay
    return result

print(solution())