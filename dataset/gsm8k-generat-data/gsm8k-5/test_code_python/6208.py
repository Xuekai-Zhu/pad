def solution():
    # Cups of flour needed for one batch of cookies
    flour_per_batch = 4

    # Cups of sugar needed for one batch of cookies
    sugar_per_batch = 1.5

    # Number of batches 
    num_batches = 8

    # Total cups of flour needed for 8 batches
    total_flour = flour_per_batch * num_batches

    # Total cups of sugar needed for 8 batches
    total_sugar = sugar_per_batch * num_batches

    # Combine total cups of flour and sugar
    combined_total = total_flour + total_sugar

    result = combined_total
    return result

print(solution())