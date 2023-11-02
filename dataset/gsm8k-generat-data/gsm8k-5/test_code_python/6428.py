def solution():
    days_per_week = 5  # Percy swims for 2 hours each day for 5 days a week
    weekend_hours = 3  # Percy also swims for 3 hours on the weekend
    weeks = 4  # Percy wants to know how many hours of swimming he does over 4 weeks

    # Calculate the total hours of swimming Percy does in a week
    weekly_hours = (2 * 2) + weekend_hours  # 2 hours before school, 2 hours after school, and 3 hours on the weekend

    # Calculate the total hours of swimming Percy does in 4 weeks
    total_hours = weekly_hours * weeks * days_per_week
    result = total_hours
    return result

print(solution())