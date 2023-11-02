def solution():
    # Calculate the total amount of sauce Jack has made
    total_sauce = 3 + 1 + 1  # cups

    # Calculate the amount of sauce used for 18 pulled pork sandwiches
    pulled_pork_sauce = 18 * (1/6)  # cups

    # Calculate the amount of sauce left over for burgers
    burger_sauce = total_sauce - pulled_pork_sauce  # cups

    # Calculate the number of burgers Jack can make with the remaining sauce
    burgers = burger_sauce / (1/4)  

    result = int(burgers)  # cast to integer since you can only make whole burgers
    return result

print(solution())