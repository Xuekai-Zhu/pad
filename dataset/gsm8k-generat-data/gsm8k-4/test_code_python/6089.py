def solution():
    """Javier is having an eating contest with his brother. It's ravioli night and there is meat ravioli, pumpkin ravioli, and cheese ravioli. The meat ravioli weighs 1.5 ounces each. The pumpkin ravioli is 1.25 ounces each. The cheese ravioli is one ounce. Javier eats 5 meat ravioli, 2 pumpkin ravioli, and 4 cheese ravioli. His brother just ate pumpkin ravioli and had 12 of them. What is the total amount of ounces eaten by the winner?"""
    # Define the weight of each type of ravioli
    MEAT_WEIGHT = 1.5
    PUMPKIN_WEIGHT = 1.25
    CHEESE_WEIGHT = 1.0

    # Calculate the total weight eaten by Javier
    javier_weight = 5 * MEAT_WEIGHT + 2 * PUMPKIN_WEIGHT + 4 * CHEESE_WEIGHT

    # Calculate the total weight eaten by Javier's brother
    brother_weight = 12 * PUMPKIN_WEIGHT

    # Determine the winner based on the total weight eaten
    if javier_weight > brother_weight:
        winner_weight = javier_weight
    else:
        winner_weight = brother_weight

    result = winner_weight
    return result

print(solution())