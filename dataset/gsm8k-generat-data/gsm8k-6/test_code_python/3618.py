def solution():
    # Calculate the total number of tasks and the number of bonus Maurice receives
    total_tasks = 30
    bonus_tasks = total_tasks // 10  

    # Calculate the total earnings for Maurice
    earnings = (2 * total_tasks) + (6 * bonus_tasks)

    result = earnings
    return result

print(solution())