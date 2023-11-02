def solution():
    
    loads_per_week = 3
    pods_per_load = 1
    pods_per_pack = 39
    weeks_per_year = 52
    total_pods = loads_per_week * pods_per_load * weeks_per_year
    pods_needed = total_pods / pods_per_pack
    result = pods_needed
    return result

print(solution())