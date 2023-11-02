def solution():
    """Joe has $50 to buy an outfit for his new field trip. 
    There is a 30% off sale at the clothing store. 
    The shirt he picks out has a price of $25. 
    He also picks out a pair of shorts for $35. 
    Assuming that sales tax is included, how much money will Joe have left after the purchase?"""
    budget = 50
    shirt_price = 25
    shorts_price = 35
    sale_percent = 30
    
    # Calculate the discounted prices with sale_percent
    discounted_shirt_price = shirt_price - (shirt_price * (sale_percent / 100))
    discounted_shorts_price = shorts_price - (shorts_price * (sale_percent / 100))
    
    # Calculate the subtotal and sales tax
    subtotal = discounted_shirt_price + discounted_shorts_price
    sales_tax = subtotal * 0.08
    
    # Calculate the total cost
    total_cost = subtotal + sales_tax
    
    # Calculate the money left after purchase
    money_left = budget - total_cost
    
    result = money_left
    return result

print(solution())