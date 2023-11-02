def solution():
    
    pansies = 5
    price_pansies = 2.50
    hydrangea = 1
    price_hydrangea = 12.50
    petunias = 5
    price_petunias = 1.00
    bill_amount = 50.00
    total_amount = pansies * price_pansies + hydrangea * price_hydrangea + petunias * price_petunias
    discount_amount = total_amount * 0.10
    total_due = total_amount - discount_amount
    change_amount = bill_amount - total_due
    result = change_amount
    
    return result

print(solution())