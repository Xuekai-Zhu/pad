def solution():
    # Calculate the total cost of Snickers and M&M's purchased by Julia
    cost_Snickers = 2 * 1.5  
    cost_MMs = 3 * 2 * 1.5  # a pack of M&M's has the same cost as 2 Snickers
    total_cost = cost_Snickers + cost_MMs

    # Calculate the amount of change Julia will receive
    amount_paid = 2 * 10  
    change = amount_paid - total_cost
    result = change
    return result

print(solution())