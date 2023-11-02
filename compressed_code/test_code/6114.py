def solution():
    
    
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