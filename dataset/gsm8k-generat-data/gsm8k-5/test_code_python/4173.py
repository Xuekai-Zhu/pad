def solution():
    # Calculate the total amount of sauce Jack can make
    total_sauce = 3 + 1 + 1  # Jack uses 3 cups of ketchup, 1 cup of vinegar and 1 cup of honey

    # Calculate the amount of sauce used for each pulled pork sandwich
    sauce_per_sandwich = 1/6

    # Calculate the amount of sauce used for each burger
    sauce_per_burger = 1/4

    # Calculate the amount of sauce used for 18 pulled pork sandwiches
    sauce_for_sandwiches = 18 * sauce_per_sandwich

    # Calculate the remaining amount of sauce for burgers
    remaining_sauce = total_sauce - sauce_for_sandwiches

    # Calculate the number of burgers Jack can make
    burgers = remaining_sauce / sauce_per_burger
    result = burgers
    return result

print(solution())