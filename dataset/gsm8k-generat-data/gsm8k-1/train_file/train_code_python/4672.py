def solution():
    """Leon ordered 3 sets of toy organizers for $78 per set and 2 gaming chairs for $83 each. If there is a delivery fee that is 5% of the total sales, how much did Leon pay?"""
    toy_organizers_price = 78
    gaming_chairs_price = 83
    number_of_toy_organizers = 3
    number_of_gaming_chairs = 2
    total_price = (toy_organizers_price * number_of_toy_organizers) + (gaming_chairs_price * number_of_gaming_chairs)
    delivery_fee = total_price * 0.05
    total_cost = total_price + delivery_fee
    result = total_cost
    return result

print(solution())