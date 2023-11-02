def solution():
    sugar_per_batch_suiters = 30  # Mason needs 30 ounces of sugar to make a batch of suckers
    sugar_per_batch_fudge = 70  # Mason needs 70 ounces of sugar to make a batch of fudge
    num_batches = 8  # Mason wants to make 8 batches of suckers

    # Calculate the total amount of sugar needed for 8 batches of suckers
    total_sugar_for_suiters = sugar_per_batch_suiters * num_batches

    # Calculate the total amount of sugar needed for 1 batch of fudge
    total_sugar_for_fudge = sugar_per_batch_fudge * num_batches

    # Calculate the total amount of sugar needed for 8 batches of fudge
    total_sugar_for_8_batches = total_sugar_for_suiters + total_sugar_for_fudge
    result = total_sugar_for_8_batches
    return result

print(solution())