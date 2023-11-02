def solution():
    total_ants = 110  # Stephen has 110 ants in his ant farm
    worker_ants = total_ants / 2  # Half of the ants are worker ants
    male_workers = worker_ants * 0.2  # 20% of the worker ants are male
    female_workers = worker_ants - male_workers  # The rest of the worker ants are female

    result = female_workers
    return result

print(solution())