def solution():
    """Gigi is baking cookies. The recipe for 1 batch of cookies calls for 2 cups of flour. She bakes 3 batches of cookies. If her bag of flour contains 20 cups of flour, how many more batches of cookies could Gigi make in the future with the remaining amount of flour?"""
    flour_per_batch = 2
    batches_baked = 3
    total_flour_used = flour_per_batch * batches_baked
    remaining_flour = 20 - total_flour_used
    future_batches = remaining_flour / flour_per_batch
    result = future_batches
    return result

print(solution())