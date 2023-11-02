def solution():
    """Miriam takes care of the flowers in the botanical garden. She works 5 hours a day and can take care of 60 different flowers in one day. How many flowers can Miriam take care of in 6 days of work?"""
    hours_per_day = 5
    flowers_per_day = 60
    days_worked = 6
    total_flowers = hours_per_day * days_worked * flowers_per_day
    result = total_flowers
    return result

print(solution())