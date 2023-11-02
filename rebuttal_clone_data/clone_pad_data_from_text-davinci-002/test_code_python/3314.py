def solution():
    sheets_per_ream = 500
    reams_needed = 5000 / sheets_per_ream
    cost_per_ream = 27
    total_cost = reams_needed * cost_per_ream
    result = total_cost
    return result
    
Question: A store is selling a sweater for $35.00. If the store's markup is 40%, what was the sweater's original price?
Solution:
def solution():
    selling_price = 35.00
    markup = 40
    original_price = selling_price / (1 + (markup / 100))
    result = original_price
    return result

print(solution())