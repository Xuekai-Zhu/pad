def solution():
    # Define the cost of muffins and fruit cups
    muffin_cost = 2
    fruit_cost = 3

    # Calculate the cost of Francis' breakfast
    francis_muffin_cost = 2 * muffin_cost
    francis_fruit_cost = 2 * fruit_cost
    francis_total_cost = francis_muffin_cost + francis_fruit_cost

    # Calculate the cost of Kiera's breakfast
    kiera_muffin_cost = 2 * muffin_cost
    kiera_fruit_cost = 1 * fruit_cost
    kiera_total_cost = kiera_muffin_cost + kiera_fruit_cost

    # Calculate the total cost of their breakfast
    total_cost = francis_total_cost + kiera_total_cost
    result = total_cost
    return result

print(solution())