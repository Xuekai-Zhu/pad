def solution():
    # Calculate the time needed to make and cook 2 pizzas
    time_per_batch = 30 + 30  # 30 minutes for dough, 30 minutes in the oven
    # Calculate the time needed to make 6 pizzas (2 batches)
    time_for_6_pizzas = time_per_batch * 2
    # Calculate the time needed to make 12 pizzas (4 batches)
    time_for_12_pizzas = time_for_6_pizzas * 2
    # Calculate the total time in hours
    total_time = time_for_12_pizzas / 60  # divided by 60 to convert minutes to hours
    result = total_time
    return result

print(solution())