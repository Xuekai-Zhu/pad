def solution():
    
    ant_count = 110
    worker_ants = ant_count / 2
    male_workers = worker_ants * 0.2
    female_workers = worker_ants - male_workers
    result = female_workers
    return result

print(solution())