def solution():
    """It takes 30 minutes to make pizza dough and another 30 minutes in the oven for the pizza to cook. If one batch of pizza dough can make 3 pizzas but the oven can only fit 2 pizzas at a time, how many hours would it take for Camilla to finish making 12 pizzas?"""
    dough_time = 30
    cook_time = 30
    pizzas_per_batch = 3
    pizzas_in_oven = 2
    total_pizzas = 12

    # Calculate how many batches of dough Camilla needs to make
    batches_of_dough = total_pizzas // pizzas_per_batch
    if total_pizzas % pizzas_per_batch != 0:
        batches_of_dough += 1

    # Calculate how many times Camilla needs to use the oven
    oven_uses = batches_of_dough // (pizzas_in_oven // pizzas_per_batch)
    if batches_of_dough % (pizzas_in_oven // pizzas_per_batch) != 0:
        oven_uses += 1

    # Calculate total time in minutes and convert to hours
    total_time = dough_time * batches_of_dough + cook_time * oven_uses
    result = total_time / 60
    return result

print(solution())