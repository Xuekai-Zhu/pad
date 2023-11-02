def solution():
    """Kyle goes to basketball practice every day for 2 hours. At practice he spends half of the time shooting and the rest of the time running and weight lifting. If he runs for twice the time he spends weightlifting, how much time in minutes does he spend lifting weight?"""
    practice_time = 2 * 60  # convert 2 hours to minutes
    shooting_time = practice_time / 2
    running_time = practice_time / 4  # since running time is twice the weightlifting time
    weightlifting_time = practice_time - shooting_time - running_time
    result = weightlifting_time
    return result

print(solution())