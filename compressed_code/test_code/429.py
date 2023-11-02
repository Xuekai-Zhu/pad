def solution():
    
    largest_rate = 3
    medium_rate = 0.5 * largest_rate
    smallest_rate = 1 / 3 * medium_rate

    total_time = 2 * 60 
    largest_leakage = largest_rate * total_time
    medium_leakage = medium_rate * total_time
    smallest_leakage = smallest_rate * total_time

    total_leakage = largest_leakage + medium_leakage + smallest_leakage
    result = total_leakage
    return result

print(solution())