def solution():
    """Jerry is trying to cut down on the amount of soda he drinks. Right now, he drinks 48 sodas a week. If he cuts the number of sodas he drinks in half each week, how many weeks will it take him to only drink 6 sodas per week?"""
    sodas_per_week = 48
    target_sodas_per_week = 6
    weeks = 0
    while sodas_per_week > target_sodas_per_week:
        sodas_per_week /= 2
        weeks += 1
    result = weeks
    return result

print(solution())