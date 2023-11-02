def solution():
    """Tim hires two bodyguards. They each charge $20 an hour. He hires them for 8 hour per day. How much does he pay them in a week if he hires them 7 days a week?"""
    hourly_rate = 20
    hours_per_day = 8
    guards = 2
    days_per_week = 7
    total_hours = guards * hours_per_day * days_per_week
    total_cost = total_hours * hourly_rate
    result = total_cost
    return result

print(solution())