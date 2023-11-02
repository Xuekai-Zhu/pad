def solution():
    minutes_per_day = 45  # Children watch 45 minutes of TV each day
    days_per_week = 4  # Children are allowed to watch TV 4 days a week
    weeks = 2  # We want to calculate how many hours of TV they watch in 2 weeks

    # Calculate the total minutes of TV watched in 2 weeks
    total_minutes = minutes_per_day * days_per_week * weeks

    # Convert the total minutes to hours
    hours = total_minutes / 60
    result = hours
    return result

print(solution())