def solution():
    entrance_fee = 20  # James pays $20 to enter the club
    drinks_for_friends = 2 * 5  # James buys 2 rounds of drinks for his 5 friends
    drinks_for_self = 6  # James buys 6 drinks for himself
    drink_price = 6  # Each drink costs $6
    food_price = 14  # Fried chicken costs $14
    tip_percent = 0.3  # James leaves a 30% tip

    # Calculate the total cost of drinks and food before tip
    total_cost_before_tip = entrance_fee + (drinks_for_friends + drinks_for_self) * drink_price + food_price

    # Calculate the tip amount
    tip_amount = total_cost_before_tip * tip_percent

    # Calculate the total cost with tip
    total_cost_with_tip = total_cost_before_tip + tip_amount

    result = total_cost_with_tip
    return result

print(solution())