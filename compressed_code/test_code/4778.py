def solution():
    
    flour_per_batch = 2
    batches_baked = 3
    total_flour_used = flour_per_batch * batches_baked
    remaining_flour = 20 - total_flour_used
    future_batches = remaining_flour / flour_per_batch
    result = future_batches
    return result

print(solution())