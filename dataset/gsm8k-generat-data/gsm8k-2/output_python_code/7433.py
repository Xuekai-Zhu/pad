def solution():
    """Travis has 10000 apples, and he is planning to sell these apples in boxes. Fifty apples can fit in each box. If he sells each box of apples for $35, how much will he be able to take home?"""
    total_apples = 10000
    apples_per_box = 50
    boxes = total_apples // apples_per_box
    box_price = 35
    total_earnings = boxes * box_price
    result = total_earnings
    return result

print(solution())