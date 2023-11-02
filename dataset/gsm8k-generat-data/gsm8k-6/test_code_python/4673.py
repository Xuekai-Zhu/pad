def solution():
    # Calculate the total cost of the toy organizers
    toy_organizer_cost = 78 * 3

    # Calculate the total cost of the gaming chairs
    gaming_chair_cost = 83 * 2

    # Calculate the subtotal cost
    subtotal_cost = toy_organizer_cost + gaming_chair_cost

    # Calculate the delivery fee
    delivery_fee = 0.05 * subtotal_cost

    # Calculate the total cost
    total_cost = subtotal_cost + delivery_fee

    result = total_cost
    return result

print(solution())