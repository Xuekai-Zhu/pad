def solution():
    num_ants = 110
    worker_ants_frac = 0.5  # Half of the ants are worker ants
    male_worker_frac = 0.2  # 20% of the worker ants are male

    # Calculate the number of worker ants
    num_worker_ants = num_ants * worker_ants_frac

    # Calculate the number of male worker ants
    num_male_worker_ants = num_worker_ants * male_worker_frac

    # Calculate the number of female worker ants
    num_female_worker_ants = num_worker_ants - num_male_worker_ants
    result = num_female_worker_ants
    return result

print(solution())