def solution():
    
    guests = 20
    hushpuppies_per_guest = 5
    total_hushpuppies = guests * hushpuppies_per_guest
    hushpuppies_per_batch = 10
    time_per_batch = 8
    batches_needed = total_hushpuppies // hushpuppies_per_batch + \
        (1 if total_hushpuppies % hushpuppies_per_batch != 0 else 0)
    total_time = batches_needed * time_per_batch
    result = total_time
    return result

print(solution())