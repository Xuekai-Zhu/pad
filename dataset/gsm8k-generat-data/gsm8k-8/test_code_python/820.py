def solution():
    # Calculate the total cost of the meal
    total_cost = 16 + 14
    
    # Calculate the amount James needs to pay before the tip
    james_half_bill = total_cost / 2
    
    # Calculate the amount of the tip
    tip_amount = james_half_bill * 0.2
    
    # Calculate the total amount James needs to pay
    james_total = james_half_bill + tip_amount
    
    result = james_total
    return result

print(solution())