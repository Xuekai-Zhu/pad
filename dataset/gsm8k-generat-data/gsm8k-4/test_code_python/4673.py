def solution():
    """Leon ordered 3 sets of toy organizers for $78 per set and 2 gaming chairs for $83 each. If there is a delivery fee that is 5% of the total sales, how much did Leon pay?"""
    # Define the prices of the toy organizers and the gaming chairs
    TOY_ORGANIZER_PRICE = 78
    GAMING_CHAIR_PRICE = 83

    # Calculate the total cost of the toy organizers
    total_toy_organizer_cost = 3 * TOY_ORGANIZER_PRICE

    # Calculate the total cost of the gaming chairs
    total_gaming_chair_cost = 2 * GAMING_CHAIR_PRICE

    # Calculate the subtotal
    subtotal = total_toy_organizer_cost + total_gaming_chair_cost

    # Calculate the delivery fee
    delivery_fee = subtotal * 0.05

    # Calculate the total cost
    total_cost = subtotal + delivery_fee

    result = total_cost
    return result

print(solution())