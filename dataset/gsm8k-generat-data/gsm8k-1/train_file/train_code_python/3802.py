def solution():
    """Tom decides to buy some shirts from his favorite fandoms because there is a sale on his favorite website. He buys 5 t-shirts from each of his 4 favorite fandoms. The shirts normally cost $15 each but there is a 20% off sale. The order qualified for free shipping but he still needed to pay 10% tax. How much did he pay?"""
    num_fandoms = 4
    shirts_per_fandom = 5
    shirt_price = 15
    discount_percent = 20
    tax_percent = 10
    
    # Calculate total cost of shirts before discount
    total_shirt_cost = num_fandoms * shirts_per_fandom * shirt_price
    
    # Apply discount and calculate new total cost
    final_shirt_cost = total_shirt_cost * (1 - (discount_percent / 100))
    
    # Calculate tax and add to total cost
    total_cost = final_shirt_cost * (1 + (tax_percent / 100))
    
    result = total_cost
    return result

print(solution())