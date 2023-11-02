def solution():
    num_guests = 20
    hushpuppies_per_guest = 5
    total_hushpuppies = num_guests * hushpuppies_per_guest

    hushpuppies_per_batch = 10
    time_per_batch = 8
    num_batches = total_hushpuppies / hushpuppies_per_batch
    total_time = num_batches * time_per_batch

    result = total_time
    return result

print(solution())