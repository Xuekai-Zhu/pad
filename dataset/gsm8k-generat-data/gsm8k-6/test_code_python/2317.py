def solution():
    lobster_cost = 25.50
    steak_cost = 35.00
    cheeseburger_cost = 13.50
    appetizer_cost = 8.50
    dessert_cost = 6.00
    
    total_food_cost = (lobster_cost + steak_cost + 2*cheeseburger_cost)  # cost of food items
    total_cost = total_food_cost + appetizer_cost + 4*dessert_cost  # total cost of food and drink items
    
    # Calculate the tip amount and add it to the total cost
    tip = 0.20 * total_cost
    total_cost += tip

    result = total_cost
    return result

print(solution())