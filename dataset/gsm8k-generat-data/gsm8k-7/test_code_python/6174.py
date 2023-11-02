def solution():
    cups_per_batch = 2
    num_batches = 3
    total_cups_used = cups_per_batch * num_batches
    remaining_cups = 20 - total_cups_used
    batches_possible = remaining_cups // cups_per_batch
    result = batches_possible
    return result

print(solution())