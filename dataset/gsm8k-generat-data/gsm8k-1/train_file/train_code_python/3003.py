def solution():
    """Bill is trying to decide whether to make blueberry muffins or raspberry muffins. Blueberries cost $5.00 per 6 ounce carton and raspberries cost $3.00 per 8 ounce carton. If Bill is going to make 4 batches of muffins, and each batch takes 12 ounces of fruit, how much money would he save by using raspberries instead of blueberries?"""
    
    blueberry_cost_per_ounce = 5/6
    raspberry_cost_per_ounce = 3/8
    
    total_ounces = 4 * 12
    
    blueberry_cost = blueberry_cost_per_ounce * total_ounces
    raspberry_cost = raspberry_cost_per_ounce * total_ounces
    
    money_saved = blueberry_cost - raspberry_cost
    
    result = money_saved
    return result

print(solution())