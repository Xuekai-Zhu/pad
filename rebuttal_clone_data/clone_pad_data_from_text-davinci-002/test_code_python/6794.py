def solution():
    muffin_cost = 2
    fruit_cup_cost = 3
    francis_muffins = 2
    francis_fruit_cups = 2
    kiera_muffins = 2
    kiera_fruit_cups = 1
    francis_total = (francis_muffins * muffin_cost) + (francis_fruit_cups * fruit_cup_cost)
    kiera_total = (kiera_muffins * muffin_cost) + (kiera_fruit_cups * fruit_cup_cost)
    breakfast_cost = francis_total + kiera_total
    result = breakfast_cost
    return result

print(solution())