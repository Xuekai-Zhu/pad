def solution():
    burgers_per_guest = 1.5  # Half of the guests want 2 burgers, and the other half want 1, so the average is 1.5 burgers per guest
    total_burgers = 30 * burgers_per_guest  # Carly has 30 guests in total

    # Calculate the number of batches of 5 burgers Carly needs to cook
    batches = total_burgers / 5
    full_batches = int(batches)  # Carly can only cook full batches of 5 burgers
    partial_batch = batches - full_batches  # Carly may have a partial batch left over

    # Calculate the total cooking time for full batches
    time_for_full_batches = full_batches * 2 * 4  # Each batch takes 2 flips of 4 minutes each

    # Calculate the cooking time for the partial batch
    if partial_batch > 0:
        time_for_partial_batch = 2 * 4  # The partial batch only needs to be flipped once on each side
    else:
        time_for_partial_batch = 0

    # Calculate the total cooking time
    total_time = time_for_full_batches + time_for_partial_batch
    result = total_time
    return result

print(solution())