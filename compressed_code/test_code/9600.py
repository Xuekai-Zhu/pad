def solution():
    
    lemons_cost = 2
    papayas_cost = 1
    mangos_cost = 4
    discount_frequency = 4
    discount_amount = 1
    
    lemons_qty = 6
    papayas_qty = 4
    mangos_qty = 2
    
    total_fruits = lemons_qty + papayas_qty + mangos_qty
    total_cost = (lemons_qty * lemons_cost) + (papayas_qty * papayas_cost) + (mangos_qty * mangos_cost)
    
    if total_fruits >= discount_frequency:
        discount = (total_fruits // discount_frequency) * discount_amount
        
        total_cost -= discount
    
    result = total_cost
    return result

print(solution())