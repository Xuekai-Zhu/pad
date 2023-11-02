def solution():
    num_toy_sets = 3
    toy_set_price = 78

    num_gaming_chairs = 2
    gaming_chair_price = 83

    delivery_fee_percentage = 0.05

    # Calculate the total cost of all toy sets
    total_toy_set_cost = num_toy_sets * toy_set_price

    # Calculate the total cost of all gaming chairs
    total_gaming_chair_cost = num_gaming_chairs * gaming_chair_price

    # Calculate the subtotal
    subtotal = total_toy_set_cost + total_gaming_chair_cost

    # Calculate the delivery fee
    delivery_fee = subtotal * delivery_fee_percentage

    # Calculate the total cost
    total_cost = subtotal + delivery_fee
    result = total_cost
    return result

print(solution())