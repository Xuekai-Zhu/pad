def solution():
    meat_weight = 1.5
    pumpkin_weight = 1.25
    cheese_weight = 1

    javier_meat = 5
    javier_pumpkin = 2
    javier_cheese = 4

    brother_pumpkin = 12

    # Calculate the total amount of ounces Javier ate
    javier_total_ounces = (javier_meat * meat_weight) + \
                          (javier_pumpkin * pumpkin_weight) + \
                          (javier_cheese * cheese_weight)

    # Calculate the total amount of ounces his brother ate
    brother_total_ounces = brother_pumpkin * pumpkin_weight

    # Determine who ate more and return the total amount of ounces eaten by the winner
    if javier_total_ounces > brother_total_ounces:
        result = javier_total_ounces
    else:
        result = brother_total_ounces
    return result

print(solution())