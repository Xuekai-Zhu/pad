def solution():
    monday_delivery = 20
    tuesday_delivery = monday_delivery * 2
    wednesday_delivery = tuesday_delivery / 4
    total_delivery = monday_delivery + tuesday_delivery + wednesday_delivery
    cost_per_yard = 2
    revenue = total_delivery * cost_per_yard
    result = revenue 
    return result

print(solution())