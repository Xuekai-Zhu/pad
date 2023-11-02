def solution():
    """Tom decides to start running 5 days a week to lose weight. He runs 1.5 hours each day. He runs at a speed of 8 mph. How many miles does he run a week?"""
    days_per_week = 5
    hours_per_day = 1.5
    speed = 8
    distance = speed * hours_per_day
    weekly_distance = distance * days_per_week
    result = weekly_distance
    return result

print(solution())