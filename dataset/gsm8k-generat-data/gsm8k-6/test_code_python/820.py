def solution():
    # Calculate the total cost of the meal (before tip)
    total_cost = 16 + 14  # James orders a steak & egg meal for $16 while his friend orders chicken fried steak for $14
    
    # Calculate the amount of the tip (20% of the total cost)
    tip = 0.2 * total_cost
    
    # Calculate the total amount James has to pay (including the tip and half of the bill)
    james_share = (total_cost + tip) / 2
    
    result = james_share
    return result

print(solution())