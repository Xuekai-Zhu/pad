def solution():
    """One batch of cookies requires 4 cups of flour and 1.5 cups of sugar. How many cups of flour and sugar combined would be needed for 8 batches?"""
    # Define the amount of flour and sugar needed per batch
    FLOUR_PER_BATCH = 4
    SUGAR_PER_BATCH = 1.5

    # Calculate the total amount of flour and sugar needed for 8 batches
    total_flour = FLOUR_PER_BATCH * 8
    total_sugar = SUGAR_PER_BATCH * 8
    total_combined = total_flour + total_sugar

    # Display the total amount of flour and sugar combined
    result = total_combined
    return result

print(solution())