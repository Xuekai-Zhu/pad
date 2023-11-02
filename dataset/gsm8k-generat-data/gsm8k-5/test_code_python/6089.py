def solution():
    # Calculate the total weight of ravioli eaten by Javier
    meat_weight = 1.5 * 5  # Javier ate 5 meat ravioli, each weighing 1.5 ounces
    pumpkin_weight = 1.25 * 2  # Javier ate 2 pumpkin ravioli, each weighing 1.25 ounces
    cheese_weight = 1 * 4  # Javier ate 4 cheese ravioli, each weighing 1 ounce
    javier_weight = meat_weight + pumpkin_weight + cheese_weight

    # Calculate the total weight of ravioli eaten by Javier's brother
    brother_weight = 1.25 * 12  # Javier's brother ate 12 pumpkin ravioli, each weighing 1.25 ounces

    # Determine who ate more ravioli and return the appropriate weight
    if javier_weight > brother_weight:
        result = javier_weight
    else:
        result = brother_weight
    return result

print(solution())