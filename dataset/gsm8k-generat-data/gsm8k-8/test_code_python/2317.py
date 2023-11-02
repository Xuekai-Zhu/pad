def solution():
    # Calculate the total cost of the meals
    lobster_cost = 25.50
    steak_cost = 35.00
    burger_cost = 13.50
    appetizer_cost = 8.50
    dessert_cost = 6.00
    total_meal_cost = lobster_cost + steak_cost + 2 * burger_cost

    # Calculate the total cost of the extras
    total_extras_cost = 4 * (appetizer_cost + 4 * dessert_cost)

    # Calculate the total bill before tip
    total_bill = total_meal_cost + total_extras_cost

    # Calculate the tip
    tip = total_bill * 0.20

    # Calculate the final bill total
    final_bill_total = total_bill + tip
    result = final_bill_total
    return result

print(solution())