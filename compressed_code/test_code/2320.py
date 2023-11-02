def solution():
    
    total_burgers = 30 * 1.5
    burgers_per_batch = 5
    batches_needed = total_burgers / burgers_per_batch
    cooking_time_per_batch = 4 * 2  
    total_cooking_time = batches_needed * cooking_time_per_batch
    result = total_cooking_time
    return result

print(solution())