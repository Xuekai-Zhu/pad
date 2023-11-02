def solution():
    """Stephen has 110 ants in his ant farm. Half of the ants are worker ants, 20 percent of the worker ants are male. How many female worker ants are there?"""
    ant_count = 110
    worker_ants = ant_count / 2
    male_workers = worker_ants * 0.2
    female_workers = worker_ants - male_workers
    result = female_workers
    return result

print(solution())