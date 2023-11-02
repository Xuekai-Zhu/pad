def solution():
    """Gigi is baking cookies. The recipe for 1 batch of cookies calls for 2 cups of flour. She bakes 3 batches of cookies. If her bag of flour contains 20 cups of flour, how many more batches of cookies could Gigi make in the future with the remaining amount of flour?"""
    # Define the amount of flour needed for 1 batch of cookies and the number of batches Gigi bakes
    FLOUR_PER_BATCH = 2
    BATCHES_BAKED = 3

    # Define the total amount of flour Gigi has
    total_flour = 20

    # Calculate the amount of flour used for the batches baked
    flour_used = FLOUR_PER_BATCH * BATCHES_BAKED

    # Calculate the amount of flour remaining
    flour_remaining = total_flour - flour_used

    # Calculate the number of batches that can be made with the remaining flour
    batches_remaining = flour_remaining // FLOUR_PER_BATCH

    # return the result
    result = batches_remaining
    return result

print(solution())