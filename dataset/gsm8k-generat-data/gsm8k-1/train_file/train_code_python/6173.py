def solution():
    """Gigi is baking cookies. The recipe for 1 batch of cookies calls for 2 cups of flour. She bakes 3 batches of cookies. If her bag of flour contains 20 cups of flour, how many more batches of cookies could Gigi make in the future with the remaining amount of flour?"""
    cups_per_batch = 2
    batches_made = 3
    total_cups_used = cups_per_batch * batches_made
    cups_remaining = 20 - total_cups_used
    batches_possible = cups_remaining / cups_per_batch
    result = batches_possible
    return result

print(solution())