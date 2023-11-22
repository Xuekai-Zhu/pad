def solution():
    
    # Define the amount of sugar needed for each batch of suckers and fudge
    SUCKERS_PER_BATCH = 30
    FUCKERS_PER_BATCH = 70

    # Define the number of batches of suckers and fudge to be made
    suckers_batches = 8
    fudge_batches = 1

    # Calculate the total amount of sugar needed for suckers and fudge
    suckers_sugar = suckers_batches * SUCKERS_PER_BATCH
    fudge_sugar = fudge_batches * FUCKERS_PER_BATCH
    total_sugar = suckers_sugar + fudge_sugar

    # Display the total amount of sugar needed
    result = total_sugar
    return result

print(solution())