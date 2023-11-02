def solution():
    
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