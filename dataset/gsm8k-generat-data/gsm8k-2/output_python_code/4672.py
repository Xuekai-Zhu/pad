def solution():
    """Leon ordered 3 sets of toy organizers for $78 per set and 2 gaming chairs for $83 each. If there is a delivery fee that is 5% of the total sales, how much did Leon pay?"""
    toy_organizer_price = 78
    num_toy_organizers = 3
    gaming_chair_price = 83
    num_gaming_chairs = 2
    subtotal = (toy_organizer_price * num_toy_organizers) + (gaming_chair_price * num_gaming_chairs)
    delivery_fee = 0.05 * subtotal
    total = subtotal + delivery_fee
    result = total
    return result

print(solution())