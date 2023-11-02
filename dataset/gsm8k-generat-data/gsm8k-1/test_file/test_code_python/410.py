def solution():
    """Misha picks out 4 blouses from the 30% off rack. The regular price for each blouse is $20. How much is the total cost of the discounted blouses?"""
    blouses_picked = 4
    discount_percent = 30
    regular_price = 20
    discounted_price = regular_price - (regular_price * (discount_percent / 100))
    total_cost = blouses_picked * discounted_price
    result = total_cost
    
    return result

print(solution())