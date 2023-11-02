def solution():
    """Gigi is baking cookies. The recipe for 1 batch of cookies calls for 2 cups of flour. She bakes 3 batches of cookies. If her bag of flour contains 20 cups of flour, how many more batches of cookies could Gigi make in the future with the remaining amount of flour?"""
    # Define the amount of flour needed for 1 batch of cookies
    FLOUR_PER_BATCH = 2

    # Define the number of batches Gigi bakes
    batches_baked = 3

    # Define the amount of flour Gigi has
    flour_available = 20

    # Calculate the amount of flour used for the batches Gigi baked
    flour_used = batches_baked * FLOUR_PER_BATCH

    # Calculate the amount of flour remaining
    flour_remaining = flour_available - flour_used

    # Calculate the number of batches Gigi can make with the remaining flour
    batches_remaining = flour_remaining // FLOUR_PER_BATCH

    # Display the number of batches Gigi can make
    result = batches_remaining
    return result

print(solution())