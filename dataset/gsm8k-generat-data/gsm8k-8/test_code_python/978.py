def solution():
    total_ants = 110
    worker_ants = total_ants / 2
    male_workers = worker_ants * 0.2
    female_workers = worker_ants - male_workers
    result = female_workers
    return result

print(solution())