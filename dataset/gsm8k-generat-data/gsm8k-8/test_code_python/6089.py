def solution():
    # Calculate the total weight of meat ravioli eaten by Javier
    meat_weight = 5 * 1.5

    # Calculate the total weight of pumpkin ravioli eaten by Javier
    pumpkin_weight = 2 * 1.25

    # Calculate the total weight of cheese ravioli eaten by Javier
    cheese_weight = 4 * 1

    # Calculate the total weight of ravioli eaten by Javier
    javier_weight = meat_weight + pumpkin_weight + cheese_weight

    # Calculate the total weight of pumpkin ravioli eaten by Javier's brother
    brother_weight = 12 * 1.25

    # Determine who ate more and calculate the total weight eaten by the winner
    if javier_weight > brother_weight:
        result = javier_weight
    else:
        result = brother_weight

    return result

print(solution())