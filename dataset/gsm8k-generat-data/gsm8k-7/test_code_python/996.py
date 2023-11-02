def solution():
    entrance_fee = 20
    num_friends = 5
    num_rounds = 2
    num_drinks = 6
    drink_price = 6
    food_price = 14
    tip_percentage = 0.3

    # Calculate the total cost of all drinks
    total_drink_cost = num_drinks * drink_price

    # Calculate the total cost of all rounds of drinks for James and his friends
    total_round_cost = num_rounds * num_friends * drink_price

    # Calculate the subtotal by adding up all costs except for tip and entrance fee
    subtotal = entrance_fee + total_drink_cost + total_round_cost + food_price

    # Calculate the total tip amount
    tip_amount = subtotal * tip_percentage

    # Calculate the total cost including tip
    total_cost = subtotal + tip_amount
    result = total_cost
    return result

print(solution())