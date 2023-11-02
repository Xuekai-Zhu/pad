def solution():
    daily_run = 60
    thursday_run = 40  # 60 - 20 minutes
    friday_run = 70  # 60 + 10 minutes
    total_run = 0

    # Calculate the total run time for Monday to Wednesday
    for i in range(3):
        total_run += daily_run

    # Add Thursday and Friday's run time to the total
    total_run += thursday_run + friday_run

    result = total_run
    return result

print(solution())