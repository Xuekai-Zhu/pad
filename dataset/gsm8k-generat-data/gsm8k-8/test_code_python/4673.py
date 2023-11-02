def solution():
    # Calculate the total cost of the toy organizers
    toy_organizers_cost = 3 * 78

    # Calculate the total cost of the gaming chairs
    gaming_chairs_cost = 2 * 83

    # Calculate the subtotal
    subtotal = toy_organizers_cost + gaming_chairs_cost

    # Calculate the delivery fee
    delivery_fee = 0.05 * subtotal

    # Calculate the total cost
    total_cost = subtotal + delivery_fee

    result = total_cost
    return result

print(solution())