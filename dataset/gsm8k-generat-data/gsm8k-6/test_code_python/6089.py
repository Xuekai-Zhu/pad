def solution():
    # Calculate the total ounces eaten by Javier
    ounces_javier = (5 * 1.5) + (2 * 1.25) + (4 * 1)  # Javier eats 5 meat, 2 pumpkin, and 4 cheese ravioli

    # Calculate the total ounces eaten by Javier's brother
    ounces_brother = 12 * 1.25  # Javier's brother eats 12 pumpkin ravioli

    # Determine the winner
    if ounces_javier > ounces_brother:
        result = ounces_javier
    else:
        result = ounces_brother

    return result

print(solution())