def solution():
    """Pearl wants to order 5 monogrammed Christmas stockings for each of her 5 grandchildren and her own 4 children. The stockings are $20.00 each and currently 10% off. The monogramming will costs $5.00 per stocking. How much will the stockings costs?"""
    num_stockings = 5 * 5 + 4
    stocking_price = 20 * 0.9
    monogram_price = 5
    total_price = num_stockings * (stocking_price + monogram_price)
    result = total_price
    return result

print(solution())