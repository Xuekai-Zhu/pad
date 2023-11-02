def solution():
    """Carly is making burgers for a neighborhood BBQ. Each burger needs to be cooked for 4 minutes on each side. Carly can fit 5 burgers on the grill at once. If half her 30 guests want 2 burgers and the other half each want 1, how long will it take Carly to cook all the burgers?"""
    # Calculate the total number of burgers needed
    num_double_burgers = 15
    num_single_burgers = 15
    total_burgers = num_double_burgers * 2 + num_single_burgers

    # Calculate the total time to cook all the burgers
    time_per_burger = 4  # minutes
    burgers_per_batch = 5
    batches_needed = total_burgers // burgers_per_batch + int(total_burgers % burgers_per_batch > 0) # round up
    total_time = batches_needed * time_per_burger * 2  # burgers need to be flipped

    # Display the total time
    result = total_time
    return result

print(solution())