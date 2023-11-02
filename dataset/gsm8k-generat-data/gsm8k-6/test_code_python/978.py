def solution():
    # Find the number of worker ants
    worker_ants = 110 / 2

    # Find the number of male worker ants
    male_worker_ants = worker_ants * 0.20

    # Find the number of female worker ants
    female_worker_ants = worker_ants - male_worker_ants
    result = female_worker_ants
    return result

print(solution())