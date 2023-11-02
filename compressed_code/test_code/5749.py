def solution():
    
    total_benches = 50
    capacity_per_bench = 4
    people_sitting = 80
    total_capacity = total_benches * capacity_per_bench
    occupied_capacity = people_sitting
    available_capacity = total_capacity - occupied_capacity
    result = available_capacity
    return result

print(solution())