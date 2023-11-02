def solution():
    
    asparagus_price = 3.00
    grape_price = 2.50
    apple_price = 0.50
    asparagus_bundle = 60
    grape_box = 40
    apple_quantity = 700
    total_asparagus_price = asparagus_price * asparagus_bundle
    total_grape_price = grape_price * grape_box
    total_apple_price = apple_price * apple_quantity
    total_price = total_asparagus_price + total_grape_price + total_apple_price
    result = total_price
    return result

print(solution())