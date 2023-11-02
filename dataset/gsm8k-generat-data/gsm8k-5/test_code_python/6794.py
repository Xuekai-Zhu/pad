def solution():
    # Calculate the cost of Francis' order
    francis_muffin_cost = 2 * 2  # Francis had 2 muffins, which cost $2 each
    francis_fruit_cost = 3 * 2  # Francis had 2 fruit cups, which cost $3 each
    francis_total_cost = francis_muffin_cost + francis_fruit_cost

    # Calculate the cost of Kiera's order
    kiera_muffin_cost = 2 * 2  # Kiera had 2 muffins, which cost $2 each
    kiera_fruit_cost = 3 * 1  # Kiera had 1 fruit cup, which cost $3 each
    kiera_total_cost = kiera_muffin_cost + kiera_fruit_cost

    # Calculate the total cost of their breakfast
    total_cost = francis_total_cost + kiera_total_cost
    result = total_cost
    return result

print(solution())