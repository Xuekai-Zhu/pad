def solution():
    """Travis has 10000 apples, and he is planning to sell these apples in boxes. Fifty apples can fit in each box. If he sells each box of apples for $35, how much will he be able to take home?"""
    num_apples = 10000
    apples_per_box = 50
    boxes = num_apples // apples_per_box
    box_price = 35
    total_profit = boxes * box_price
    result = total_profit
    return result

print(solution())