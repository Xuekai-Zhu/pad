def solution():
    start_time = 5.0 # in hours (equivalent to 5:00 pm)
    dinner_time = start_time + 0.75 # 45 minutes for dinner
    homework_time = dinner_time + 0.5 # 30 minutes for homework
    chores_time = homework_time + 1.0 # 30 minutes for cleaning room + 5 minutes for taking out the trash + 10 minutes for emptying the dishwasher
    latest_start_time = chores_time - 3.0 # subtract 3 hours to get latest start time to finish by 8 pm

    result = latest_start_time
    return result

print(solution())