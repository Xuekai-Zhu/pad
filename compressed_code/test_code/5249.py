def solution():
    
    muffin_price = 2
    fruit_price = 3
    francis_muffins = 2
    francis_fruit_cups = 2
    kiera_muffins = 2
    kiera_fruit_cups = 1
    francis_cost = (francis_muffins * muffin_price) + (francis_fruit_cups * fruit_price)
    kiera_cost = (kiera_muffins * muffin_price) + (kiera_fruit_cups * fruit_price)
    total_cost = francis_cost + kiera_cost
    result = total_cost
    return result

print(solution())