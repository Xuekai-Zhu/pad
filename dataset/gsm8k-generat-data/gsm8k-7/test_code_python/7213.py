def solution():
    john_main_meal_cost = mike_main_meal_cost = 10  # cost of Taco Grande Plate
    mike_side_salad_cost = 2
    mike_cheesy_fries_cost = 4
    mike_drink_cost = 2

    john_total_cost = john_main_meal_cost
    mike_total_cost = mike_main_meal_cost + mike_side_salad_cost + mike_cheesy_fries_cost + mike_drink_cost

    # Calculate the combined total cost
    combined_cost = john_total_cost + mike_total_cost

    result = combined_cost
    return result

print(solution())