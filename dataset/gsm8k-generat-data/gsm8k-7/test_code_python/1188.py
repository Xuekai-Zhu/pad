def solution():
    sandwich_price = 5
    delivery_fee = 20
    num_sandwiches = 18
    tip_percentage = 0.1
    
    # Calculate the cost of all sandwiches
    sandwich_cost = num_sandwiches * sandwich_price
    
    # Calculate the tip amount
    tip_amount = sandwich_cost * tip_percentage
    
    # Calculate the total amount received by Preston
    total_amount = sandwich_cost + delivery_fee + tip_amount
    result = total_amount
    return result

print(solution())