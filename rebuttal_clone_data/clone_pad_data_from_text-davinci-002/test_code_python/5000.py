def solution():
    hamburger_meat = 5.00
    crackers = 3.50
    vegetables = 2.00
    cheese = 3.50
    discount = 0.10
    
    total_bill = hamburger_meat + crackers + (vegetables * 4) + cheese
    total_bill_discounted = total_bill - (total_bill * discount)
    
    result = total_bill_discounted
    return result

print(solution())