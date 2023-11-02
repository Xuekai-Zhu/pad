def solution():
    total_sugar = 3 + (2 * 6)
    sugar_needed_per_batch = 1
    sugar_needed_for_frosting = 2
    total_batch_size = total_sugar / sugar_needed_per_batch
    total_frosting_size = total_sugar / sugar_needed_for_frosting
    cupcakes_baked = total_batch_size / 12
    cupcakes_frosted = total_frosting_size / 12
    result = min(cupcakes_baked, cupcakes_frosted)
    return result

print(solution())