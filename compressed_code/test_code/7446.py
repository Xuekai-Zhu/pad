def solution():
    
    bill_amount = 50
    pizza_cost = 12
    juice_cost = 2
    total_cost = (2 * pizza_cost) + (2 * juice_cost)
    change_amount = bill_amount - total_cost
    result = change_amount
    return result

print(solution())