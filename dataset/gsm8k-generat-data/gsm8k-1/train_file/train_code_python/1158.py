def solution():
    """Erwan went on shopping. He purchased a pair of shoes at $200 but discounted 30%, and two shirts at $80 each. Upon checkout, the cashier said that there is an additional 5% discount. How much did he spend after all the discounts?"""
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