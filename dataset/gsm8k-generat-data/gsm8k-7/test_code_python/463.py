def solution():
    time_per_pizza = 60  # 30 minutes for dough + 30 minutes in the oven
    pizzas_per_batch = 3
    max_pizzas_in_oven = 2
    total_pizzas = 12

    # Calculate the total number of batches needed to make all the pizzas
    total_batches = total_pizzas // pizzas_per_batch
    if total_pizzas % pizzas_per_batch > 0:
        total_batches += 1

    # Calculate the total time needed to make all the pizzas
    total_time = total_batches * time_per_pizza * (max_pizzas_in_oven / pizzas_per_batch)

    # Convert the total time to hours
    total_hours = total_time / 60
    result = total_hours
    return result

print(solution())