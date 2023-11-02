def solution():
    
    shoe_price = 200
    shoe_discount = 0.30
    shirt_price = 80
    num_shirts = 2
    additional_discount = 0.05
    
    discounted_shoe_price = shoe_price * (1 - shoe_discount)
    total_shirt_price = shirt_price * num_shirts
    
    subtotal = discounted_shoe_price + total_shirt_price
    total_discount = subtotal * additional_discount
    final_price = subtotal - total_discount
    
    result = final_price
    return result

print(solution())