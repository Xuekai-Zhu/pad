def solution():
    """Kat decides she wants to start a boxing career. She gets a gym membership and spends 1 hour in the gym 3 times a week doing strength training. She also trained at the boxing gym 4 times a week for 1.5 hours. How many hours a week does she train?"""
    gym_hours_per_day = 1
    gym_days_per_week = 3
    boxing_hours_per_day = 1.5
    boxing_days_per_week = 4
    total_gym_hours = gym_hours_per_day * gym_days_per_week
    total_boxing_hours = boxing_hours_per_day * boxing_days_per_week
    total_hours = total_gym_hours + total_boxing_hours
    result = total_hours
    return result

print(solution())