def solution():
    
    original_price_per_head = 204000 / (340 - 172)
    lowered_price_per_head = original_price_per_head - 150
    remaining_cattle = 340 - 172
    original_revenue = remaining_cattle * original_price_per_head
    lowered_revenue = remaining_cattle * lowered_price_per_head
    loss = original_revenue - lowered_revenue
    result = loss
    return result

print(solution())