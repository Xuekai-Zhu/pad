def solution():
    flour_per_batch = 4
    sugar_per_batch = 1.5
    num_batches = 8

    # Calculate the total amount of flour needed for 8 batches
    total_flour = flour_per_batch * num_batches

    # Calculate the total amount of sugar needed for 8 batches
    total_sugar = sugar_per_batch * num_batches

    # Calculate the combined amount of flour and sugar needed for 8 batches
    total_flour_and_sugar = total_flour + total_sugar
    result = total_flour_and_sugar
    return result

print(solution())