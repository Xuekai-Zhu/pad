def solution():
    taco_shell_cost = 5
    num_bell_peppers = 4
    bell_pepper_cost = 1.5
    num_pounds_meat = 2
    meat_cost_per_pound = 3

    # Calculate the total cost of the taco shells
    total_taco_shell_cost = taco_shell_cost

    # Calculate the total cost of the bell peppers
    total_bell_pepper_cost = num_bell_peppers * bell_pepper_cost

    # Calculate the total cost of the meat
    total_meat_cost = num_pounds_meat * meat_cost_per_pound

    # Calculate the total cost of all items
    total_cost = total_taco_shell_cost + total_bell_pepper_cost + total_meat_cost
    result = total_cost
    return result

print(solution())