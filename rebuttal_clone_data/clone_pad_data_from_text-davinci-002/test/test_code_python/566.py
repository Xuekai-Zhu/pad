def solution():
     total_ants = 110
     worker_ants = total_ants / 2
     male_worker_ants = worker_ants * 0.2
     female_worker_ants = worker_ants - male_worker_ants
     result = female_worker_ants
     return result

print(solution())