def solution():
    # Calculate the total cost of the items
    cost_hamburger_meat = 2 * 3.5  # 2 pounds of hamburger meat at $3.50 per pound
    cost_buns = 1.5
    cost_lettuce = 1.0
    cost_tomato = 1.5 * 2.0  # 1.5 pound tomato at $2.00 per pound
    cost_pickles = 2.5 - 1.0  # Jar of pickles costs $2.50 with a $1.00 off coupon applied
    total_cost = cost_hamburger_meat + cost_buns + cost_lettuce + cost_tomato + cost_pickles

    # Calculate the change Lauren would receive after paying with a $20 bill
    change = 20 - total_cost
    result = change
    return result

print(solution())