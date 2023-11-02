def solution():
    
    blueberry_cost_per_ounce = 5.0 / 6
    raspberry_cost_per_ounce = 3.0 / 8
    fruit_per_batch = 12
    num_batches = 4
    blueberry_cost = blueberry_cost_per_ounce * fruit_per_batch
    raspberry_cost = raspberry_cost_per_ounce * fruit_per_batch
    savings_per_batch = blueberry_cost - raspberry_cost
    total_savings = savings_per_batch * num_batches
    result = total_savings
    return result

print(solution())