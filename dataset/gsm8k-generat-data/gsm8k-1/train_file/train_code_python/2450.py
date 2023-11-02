def solution():
    """Sanya can wash 7 bath towels in one wash, which will take 1 hour. She only has 2 hours in a day to do this task. If she has 98 bath towels, how many days will she need to wash all of them?"""
    towels_per_wash = 7
    wash_time = 1
    total_wash_time = 2
    num_towels = 98
    num_washes = num_towels / towels_per_wash
    time_per_wash = wash_time
    total_time = num_washes * time_per_wash
    num_days = total_time / total_wash_time
    result = num_days
    return result

print(solution())