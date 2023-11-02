def solution():
    """It takes 30 minutes to make pizza dough and another 30 minutes in the oven for the pizza to cook. If one batch of pizza dough can make 3 pizzas but the oven can only fit 2 pizzas at a time, how many hours would it take for Camilla to finish making 12 pizzas?"""
    # Define the time to make one batch of dough and cook one pizza
    DOUGH_TIME = 30
    COOK_TIME = 30

    # Define the number of pizzas in one batch and the oven capacity
    PIZZAS_PER_BATCH = 3
    OVEN_CAPACITY = 2

    # Calculate the number of batches needed to make 12 pizzas
    total_pizzas = 12
    batches_needed = total_pizzas // PIZZAS_PER_BATCH
    if total_pizzas % PIZZAS_PER_BATCH > 0:
        batches_needed += 1

    # Calculate the time needed to make the dough and cook the pizzas
    total_time = batches_needed * (DOUGH_TIME + COOK_TIME * OVEN_CAPACITY)

    # Convert the time from minutes to hours
    total_time_hours = total_time / 60

    # return the result
    result = total_time_hours
    return result

print(solution())