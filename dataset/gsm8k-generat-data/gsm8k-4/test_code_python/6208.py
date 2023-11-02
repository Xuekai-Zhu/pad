def solution():
    """One batch of cookies requires 4 cups of flour and 1.5 cups of sugar. How many cups of flour and sugar combined would be needed for 8 batches?"""
    # Define the amount of flour and sugar needed for one batch of cookies
    flour_per_batch = 4
    sugar_per_batch = 1.5

    # Calculate the total amount of flour and sugar needed for 8 batches
    total_flour = flour_per_batch * 8
    total_sugar = sugar_per_batch * 8

    # Calculate the combined amount of flour and sugar needed
    combined_amount = total_flour + total_sugar

    result = combined_amount
    return result

print(solution())