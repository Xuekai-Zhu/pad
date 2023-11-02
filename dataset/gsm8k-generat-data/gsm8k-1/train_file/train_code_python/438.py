def solution():
    """Timothy has $50 to spend at a souvenir shop. He sees some t-shirts that cost $8 each, key chains that sell 3 pieces for $2, and bags that cost $10 each. Timothy buys 2 t-shirts and 2 bags. How many pieces of key chains can he buy with the amount of money he has left?"""
    
    total_money = 50 
    tshirt_cost = 8
    bag_cost = 10
    keychain_cost = 2/3
    
    tshirt_quantity = 2
    bag_quantity = 2
    
    total_cost = (tshirt_cost * tshirt_quantity) + (bag_cost * bag_quantity)
    
    money_left = total_money - total_cost
    
    keychain_quantity = money_left / keychain_cost 
    
    result = keychain_quantity
    
    return result

print(solution())