def solution():
    """Kyle goes to basketball practice every day for 2 hours. At practice he spends half of the time shooting and the rest of the time running and weight lifting. If he runs for twice the time he spends weightlifting, how much time in minutes does he spend lifting weight?"""
    practice_time = 2 # hours
    shooting_time = practice_time / 2
    other_time = practice_time - shooting_time
    running_time = other_time * 2 / 3
    weightlifting_time = other_time / 3
    weightlifting_time_minutes = weightlifting_time * 60
    result = weightlifting_time_minutes
    return result

print(solution())