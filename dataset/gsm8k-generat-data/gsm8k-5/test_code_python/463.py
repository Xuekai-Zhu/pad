def solution():
    time_per_batch = 30 + 30  # 30 mins to make dough, 30 mins to cook
    pizzas_per_batch = 3  # 1 batch of dough can make 3 pizzas
    pizzas_per_oven = 2  # oven can only fit 2 pizzas at a time
    total_pizzas = 12  # Camilla needs to make 12 pizzas

    # Calculate the number of batches needed to make 12 pizzas
    batches_needed = total_pizzas // pizzas_per_batch  # integer division
    if total_pizzas % pizzas_per_batch != 0:  # if there are leftover pizzas
        batches_needed += 1

    # Calculate the total time needed to make all the pizzas
    time_needed = batches_needed * time_per_batch
    # Calculate the number of hours needed, converting from minutes
    hours_needed = time_needed / 60

    result = hours_needed
    return result

print(solution())