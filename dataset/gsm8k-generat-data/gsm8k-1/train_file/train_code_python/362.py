def solution():
    """Tony paid $7 for 2 dozen apples and 1 bunch of bananas. Arnold paid $5 for 1 dozen apples and 1 bunch of bananas. How much does a bunch of bananas cost?"""
    tony_apples = 2 * 12
    tony_bananas = 1
    tony_cost = 7
    arnold_apples = 1 * 12
    arnold_bananas = 1
    arnold_cost = 5
    
    total_bananas = tony_bananas + arnold_bananas
    total_cost = tony_cost + arnold_cost
    
    cost_per_banana = (total_cost - (tony_apples + arnold_apples)) / total_bananas
    
    result = cost_per_banana
    return result

print(solution())