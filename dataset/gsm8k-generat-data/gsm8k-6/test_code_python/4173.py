def solution():
    # Calculate the total amount of barbecue sauce Jack makes
    total_sauce = 3 + 1 + 1  # Jack uses 3 cups of ketchup, 1 cup of vinegar and 1 cup of honey
    total_burger_sauce = 1/4  # Each burger takes 1/4 cup of sauce
    total_pork_sauce = 1/6  # Each pulled pork sandwich takes 1/6 cup of sauce
    total_pork = 18  # Jack is making 18 pulled pork sandwiches

    # Calculate the number of burgers Jack can make
    burgers = (total_sauce - total_pork * total_pork_sauce) / total_burger_sauce
    result = burgers
    return result

print(solution())