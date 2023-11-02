def solution():
    days = 8  # It takes 8 days for 3 builders to build a cottage
    workers = 6  # 6 workers will build the same size cottage
    # Assume that the amount of work needed to build the cottage is the same, so the ratio of workers to time is constant
    time = days * 3 / workers
    result = time
    return result

print(solution())