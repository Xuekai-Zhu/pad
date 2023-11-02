def solution():
    muffin_cost = 2
    fruit_cost = 3

    francis_muffins = 2
    francis_fruit_cups = 2
    kiera_muffins = 2
    kiera_fruit_cups = 1

    # Calculate the total cost of Francis' order
    francis_total_cost = (francis_muffins * muffin_cost) + (francis_fruit_cups * fruit_cost)

    # Calculate the total cost of Kiera's order
    kiera_total_cost = (kiera_muffins * muffin_cost) + (kiera_fruit_cups * fruit_cost)

    # Calculate the total cost of their breakfast
    total_cost = francis_total_cost + kiera_total_cost
    result = total_cost
    return result

print(solution())