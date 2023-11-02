def solution():
    """Jack is making barbecue sauce. He uses 3 cups of ketchup, 1 cup of vinegar and 1 cup of honey. If each burger takes 1/4 cup of sauce and each pulled pork sandwich takes 1/6 cup, how many burgers can Jack make if he makes 18 pulled pork sandwiches?"""
    # Calculate the total amount of sauce Jack has
    total_sauce = 3 + 1 + 1 # ketchup + vinegar + honey

    # Calculate the amount of sauce Jack uses for each pulled pork sandwich
    sauce_per_pork = 1/6

    # Calculate the amount of sauce Jack uses for each burger
    sauce_per_burger = 1/4

    # Calculate the total sauce used for the pulled pork sandwiches
    sauce_for_pork = 18 * sauce_per_pork

    # Calculate the remaining sauce Jack has after making the pulled pork sandwiches
    remaining_sauce = total_sauce - sauce_for_pork

    # Calculate the number of burgers Jack can make with the remaining sauce
    burgers = remaining_sauce / sauce_per_burger

    # Display the number of burgers Jack can make
    result = burgers
    return result

print(solution())