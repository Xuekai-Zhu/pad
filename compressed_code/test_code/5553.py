def solution():
    
    starting_amount = 65
    ice_cream_cost = 5
    tshirt_cost = (starting_amount - ice_cream_cost) / 2
    remaining_amount = starting_amount - ice_cream_cost - tshirt_cost
    deposit_amount = remaining_amount / 5
    final_amount = remaining_amount - deposit_amount
    result = final_amount
    return result

print(solution())