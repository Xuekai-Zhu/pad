def solution():
    # Calculate the time it takes to make and cook one pizza
    time_per_pizza = 30 + 30

    # Calculate how many batches of dough are needed for 12 pizzas
    batches_needed = 12 // 3
    if 12 % 3 != 0:
        batches_needed += 1

    # Calculate how many times the oven must be used per batch
    oven_uses_per_batch = batches_needed // 2
    if batches_needed % 2 != 0:
        oven_uses_per_batch += 1

    # Calculate the total time needed in hours
    total_time = time_per_pizza * 3 * batches_needed + oven_uses_per_batch * 30

    # Convert to hours and return the result
    result = total_time / 60
    return result

print(solution())