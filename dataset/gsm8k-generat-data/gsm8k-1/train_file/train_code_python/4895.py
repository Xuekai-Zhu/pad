def solution():
    """Grover bought 3 boxes of face masks. He plans to sell them for $0.50 each. If each box has 20 face masks, and he bought the 3 boxes for $15, how much will be his total profit?"""
    boxes = 3
    masks_per_box = 20
    masks_total = boxes * masks_per_box
    sale_price = 0.5
    cost = 15
    revenue = sale_price * masks_total
    profit = revenue - cost
    result = profit
    return result

print(solution())