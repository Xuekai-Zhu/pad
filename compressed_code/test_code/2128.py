def solution():
    
    flock_size = 100
    annual_change = 10 
    for i in range(5):
        flock_size += annual_change
    combined_flock_size = flock_size + 150
    result = combined_flock_size
    return result

print(solution())