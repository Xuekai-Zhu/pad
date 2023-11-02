def solution():
    # Calculate the total cost of Francis' breakfast
    francis_muffins = 2
    francis_fruit_cups = 2
    francis_total_cost = (francis_muffins * 2) + (francis_fruit_cups * 3)

    # Calculate the total cost of Kiera's breakfast
    kiera_muffins = 2
    kiera_fruit_cups = 1
    kiera_total_cost = (kiera_muffins * 2) + (kiera_fruit_cups * 3)

    # Calculate the total cost of their breakfast
    total_cost = francis_total_cost + kiera_total_cost
    result = total_cost
    return result

print(solution())