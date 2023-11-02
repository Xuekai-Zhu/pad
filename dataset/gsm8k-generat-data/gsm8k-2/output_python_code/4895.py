def solution():
    """Grover bought 3 boxes of face masks. He plans to sell them for $0.50 each. If each box has 20 face masks, and he bought the 3 boxes for $15, how much will be his total profit?"""
    masks_per_box = 20
    total_masks = masks_per_box * 3
    cost = 15
    price_per_mask = 0.5
    total_income = price_per_mask * total_masks
    profit = total_income - cost
    result = profit
    return result

print(solution())