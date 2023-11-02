def solution():
    flour_per_batch = 2
    batches_baked = 3
    flour_in_bag = 20
    flour_used = flour_per_batch * batches_baked
    flour_remaining = flour_in_bag - flour_used
    batches_possible = flour_remaining / flour_per_batch
    result = batches_possible
    return result

print(solution())