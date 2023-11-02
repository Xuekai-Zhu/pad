def solution():
    
    bags_per_time = 3
    time_per_bags = 15
    bags_needed = 8
    time_needed = (bags_needed / bags_per_time) * time_per_bags
    result = time_needed
    return result

print(solution())