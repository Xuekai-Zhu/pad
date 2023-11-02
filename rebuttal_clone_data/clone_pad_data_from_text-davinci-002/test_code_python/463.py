def solution():
    minutes_to_make_dough = 30
    minutes_to_cook = 30
    pizzas_per_batch = 3
    pizzas_baked_simultaneously = 2
    batches_needed = 4
    minutes_to_make_dough_total = minutes_to_make_dough * batches_needed
    minutes_to_cook_total = minutes_to_cook * (batches_needed * pizzas_baked_simultaneously)
    total_minutes = minutes_to_make_dough_total + minutes_to_cook_total
    hours = total_minutes / 60
    result = hours
    return result

print(solution())