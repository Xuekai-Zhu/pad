def solution():
    
    total_distance = 26
    num_checkpoints = 4
    checkpoint_distance = (total_distance - 2) / num_checkpoints
    result = checkpoint_distance
    return result

print(solution())