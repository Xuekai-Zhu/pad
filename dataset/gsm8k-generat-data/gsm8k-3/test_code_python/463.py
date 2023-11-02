def solution():
    """It takes 30 minutes to make pizza dough and another 30 minutes in the oven for the pizza to cook. If one batch of pizza dough can make 3 pizzas but the oven can only fit 2 pizzas at a time, how many hours would it take for Camilla to finish making 12 pizzas?"""
    # Define the time it takes to make dough and bake pizzas
    DOUGH_TIME = 30
    BAKE_TIME = 30

    # Define the number of pizzas per batch and the maximum number of pizzas that can fit in the oven
    PIZZAS_PER_BATCH = 3
    MAX_PIZZAS_IN_OVEN = 2

    # Calculate the number of batches needed to make 12 pizzas
    total_batches = 12 // PIZZAS_PER_BATCH
    if 12 % PIZZAS_PER_BATCH != 0:
        total_batches += 1

    # Calculate the total time it takes to make all the pizzas
    total_time = total_batches * (DOUGH_TIME + MAX_PIZZAS_IN_OVEN * BAKE_TIME)

    # Convert the total time to hours
    hours = total_time / 60

    # Display the total time in hours
    result = hours
    return result

print(solution())