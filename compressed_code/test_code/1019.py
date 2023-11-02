def solution():
    
    fabric_price = 2
    yarn_price = 3
    monday_delivery = 20
    tuesday_delivery = 2 * monday_delivery
    wednesday_delivery = tuesday_delivery / 4
    total_fabric_delivery = monday_delivery + tuesday_delivery + wednesday_delivery
    fabric_earnings = total_fabric_delivery * fabric_price
    yarn_earnings = 0 
    total_earnings = fabric_earnings + yarn_earnings
    result = total_earnings
    return result

print(solution())