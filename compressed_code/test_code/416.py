def solution():
    
    original_price = 2
    reduced_price = 1.85
    bottles = 5 * 12
    original_revenue = original_price * bottles
    reduced_revenue = reduced_price * bottles
    difference = original_revenue - reduced_revenue
    gift_cost = difference
    result = gift_cost
    return result

print(solution())