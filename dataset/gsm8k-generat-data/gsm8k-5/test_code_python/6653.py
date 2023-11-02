def solution():
    cups_of_sugar_at_home = 3
    bags_of_sugar_bought = 2
    cups_of_sugar_per_bag = 6
    cups_of_sugar_total = cups_of_sugar_at_home + (bags_of_sugar_bought * cups_of_sugar_per_bag)

    cups_of_sugar_for_batter_per_dozen = 1
    cups_of_sugar_for_frosting_per_dozen = 2

    cupcakes_per_dozen = 12

    # Determine how many dozens of cupcakes can be made with available sugar
    dozens_of_cupcakes = min(cups_of_sugar_total // cups_of_sugar_for_batter_per_dozen,
                             cups_of_sugar_total // cups_of_sugar_for_frosting_per_dozen)

    # Determine how many dozens of cupcakes can be iced with available sugar
    dozens_of_cupcakes_iced = min(cups_of_sugar_total // cups_of_sugar_for_frosting_per_dozen,
                                  dozens_of_cupcakes)

    result = dozens_of_cupcakes_iced
    return result

print(solution())