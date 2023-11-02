def solution():
    
    num_cans = 60
    space_per_can = 30
    compacted_space_percentage = 20
    compacted_space = space_per_can * (compacted_space_percentage / 100)
    total_compacted_space = num_cans * compacted_space
    result = total_compacted_space
    return result

print(solution())