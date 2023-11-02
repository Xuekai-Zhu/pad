def solution():
    """Jack is making barbecue sauce. He uses 3 cups of ketchup, 1 cup of vinegar and 1 cup of honey. If each burger takes 1/4 cup of sauce and each pulled pork sandwich takes 1/6 cup, how many burgers can Jack make if he makes 18 pulled pork sandwiches?"""
    # Define the amount of each ingredient used in the sauce
    ketchup = 3
    vinegar = 1
    honey = 1

    # Calculate the total amount of sauce made
    total_sauce = ketchup + vinegar + honey

    # Calculate the amount of sauce used for each pulled pork sandwich
    pulled_pork_sauce = 1/6

    # Calculate the total amount of sauce used for all pulled pork sandwiches
    total_pulled_pork_sauce = pulled_pork_sauce * 18

    # Calculate the amount of sauce remaining for burgers
    burger_sauce = total_sauce - total_pulled_pork_sauce

    # Calculate the number of burgers that can be made with the remaining sauce
    burgers = burger_sauce / (1/4)

    # Return the result
    result = int(burgers)
    return result

print(solution())