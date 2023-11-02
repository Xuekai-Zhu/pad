def solution():
    
    total_photos = 210
    photos_per_batch = 7
    batches_per_day = 6
    days_to_finish = total_photos / (photos_per_batch * batches_per_day)
    result = days_to_finish
    return result

print(solution())