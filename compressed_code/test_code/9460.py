def solution():
    
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