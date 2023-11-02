def solution():
    num_ketchup_cups = 3
    num_vinegar_cups = 1
    num_honey_cups = 1
    num_pp_sandwiches = 18

    # Calculate the total amount of sauce Jack can make
    total_sauce = num_ketchup_cups + num_vinegar_cups + num_honey_cups

    # Calculate how many burgers Jack can make with the total sauce he has
    num_burgers = int(total_sauce / 0.25)

    # Calculate how many pulled pork sandwiches Jack can make
    num_sandwiches = num_pp_sandwiches

    result = num_burgers
    return result

print(solution())