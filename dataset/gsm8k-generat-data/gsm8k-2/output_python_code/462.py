def solution():
    """It takes 30 minutes to make pizza dough and another 30 minutes in the oven for the pizza to cook. If one batch of pizza dough can make 3 pizzas but the oven can only fit 2 pizzas at a time, how many hours would it take for Camilla to finish making 12 pizzas?"""
    dough_time = 30
    bake_time = 30
    batch_size = 3
    oven_size = 2
    total_pizzas = 12
    batches_needed = total_pizzas // batch_size + (1 if total_pizzas % batch_size > 0 else 0)
    oven_runs_needed = batches_needed // (oven_size // batch_size) + (1 if batches_needed % (oven_size // batch_size) > 0 else 0)
    total_time = oven_runs_needed * bake_time + batches_needed * dough_time
    result = total_time / 60
    return result

print(solution())