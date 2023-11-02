def solution():

    # Define prices
    burger_price = 5
    fries_price = 3
    drink_price = 3
    burger_meal_price = 9.5
    kid_burger_price = 3
    kid_fries_price = 2
    juice_price = 2
    kid_meal_price = 5

    # Calculate total cost of individual items
    total_individual_cost = (2 * burger_price) + (2 * fries_price) + (2 * drink_price) + \
                            (4 * kid_burger_price) + (4 * kid_fries_price) + (4 * juice_price)

    # Calculate total cost of meals
    total_meal_cost = (2 * burger_meal_price) + (2 * kid_meal_price)

    # Calculate amount saved
    amount_saved = total_individual_cost - total_meal_cost
    result = amount_saved
    return result

print(solution())