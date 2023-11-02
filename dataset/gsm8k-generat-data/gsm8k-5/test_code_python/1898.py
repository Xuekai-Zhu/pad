def solution():
    guests = 20  # Walter is hosting 20 guests
    hushpuppies_per_guest = 5  # Each guest will eat 5 hushpuppies
    total_hushpuppies = guests * hushpuppies_per_guest  # Total number of hushpuppies needed
    hushpuppies_per_batch = 10  # Walter can cook 10 hushpuppies in a batch
    time_per_batch = 8  # It takes 8 minutes to cook a batch

    # Calculate the total number of batches needed
    total_batches = total_hushpuppies // hushpuppies_per_batch
    if total_hushpuppies % hushpuppies_per_batch != 0:
        total_batches += 1

    # Calculate the total time needed to cook all the hushpuppies
    total_time = total_batches * time_per_batch
    result = total_time
    return result

print(solution())