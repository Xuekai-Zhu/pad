def solution():
    flour_per_batch = 2  # Gigi needs 2 cups of flour for 1 batch of cookies
    batches_made = 3  # Gigi has already made 3 batches of cookies
    total_flour_used = flour_per_batch * batches_made  # Gigi has used this much flour

    flour_remaining = 20 - total_flour_used  # Gigi has this much flour remaining
    batches_possible = flour_remaining // flour_per_batch  # Gigi can make this many batches with the remaining flour

    result = batches_possible
    return result

print(solution())