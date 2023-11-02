def solution():
    
    guests = 20
    hushpuppies_per_guest = 5
    total_hushpuppies = guests * hushpuppies_per_guest
    hushpuppies_per_batch = 10
    time_per_batch = 8 
    
    batches = total_hushpuppies / hushpuppies_per_batch
    total_time = batches * time_per_batch
    result = total_time
    
    return result

print(solution())