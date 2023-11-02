def solution():
    
    total_jerky_needed = 60
    jerky_already_made = 20
    jerky_per_batch = 10
    batches_needed = (total_jerky_needed - jerky_already_made) / jerky_per_batch
    days_needed = int(batches_needed + 0.9)  
    result = days_needed
    return result

print(solution())