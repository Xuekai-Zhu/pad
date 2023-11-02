def solution():
    price_cherries = 5 # price of a bag of cherries
    price_olives = 7 # price of a bag of olives
    discount = 0.1 # 10% discount
    bags_of_fruit = 50 # buying 50 bags of each fruit
    
    # Calculate the total price before discount
    total_price = (price_cherries + price_olives) * bags_of_fruit
    
    # Calculate the amount of discount
    amount_discount = discount * total_price
    
    # Calculate the total price after discount
    total_price_after_discount = total_price - amount_discount
    
    result = total_price_after_discount
    return result

print(solution())