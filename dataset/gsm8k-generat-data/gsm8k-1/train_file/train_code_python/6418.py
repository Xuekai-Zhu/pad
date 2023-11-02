def solution():
    """Amber is trying to decide if she wants to spend her $7 on candy or chips. She decides to buy the thing that she can get the most of. The bags of candy cost $1 and contain 12 ounces each. The bags of chips are $1.40 and contain 17 ounces each. How many ounces does she get if she buys the item that gives her the most?"""
    candy_price = 1
    candy_weight = 12
    chips_price = 1.4
    chips_weight = 17
    
    candy_ounces_per_dollar = candy_weight / candy_price
    chips_ounces_per_dollar = chips_weight / chips_price
    
    if candy_ounces_per_dollar > chips_ounces_per_dollar:
        result = candy_ounces_per_dollar
    else:
        result = chips_ounces_per_dollar
    
    return result

print(solution())