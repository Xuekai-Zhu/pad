def solution():
    """Carly is making burgers for a neighborhood BBQ. Each burger needs to be cooked for 4 minutes on each side. Carly can fit 5 burgers on the grill at once. If half her 30 guests want 2 burgers and the other half each want 1, how long will it take Carly to cook all the burgers?"""
    total_burgers = 30 * 1.5
    burgers_per_batch = 5
    batches_needed = total_burgers / burgers_per_batch
    cooking_time_per_batch = 4 * 2  # 4 minutes per side, 2 sides per burger
    total_cooking_time = batches_needed * cooking_time_per_batch
    result = total_cooking_time
    return result

print(solution())