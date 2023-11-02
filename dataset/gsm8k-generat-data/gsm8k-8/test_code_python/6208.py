def solution():
    # Define the amounts required for one batch
    flour_per_batch = 4
    sugar_per_batch = 1.5

    # Calculate the amounts required for eight batches
    flour_for_8_batches = flour_per_batch * 8
    sugar_for_8_batches = sugar_per_batch * 8

    # Calculate the combined amount of flour and sugar
    combined_amount = flour_for_8_batches + sugar_for_8_batches
    result = combined_amount
    return result

print(solution())