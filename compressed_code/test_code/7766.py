def solution():
    
    nuggets_ordered = 100
    nuggets_per_box = 20
    boxes_ordered = nuggets_ordered // nuggets_per_box + (nuggets_ordered % nuggets_per_box > 0)
    price_per_box = 4
    total_price = boxes_ordered * price_per_box
    result = total_price
    return result

print(solution())