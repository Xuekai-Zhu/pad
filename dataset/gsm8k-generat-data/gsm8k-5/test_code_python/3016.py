def solution():
    length = 10  # Length of the pool in feet
    width = 8  # Width of the pool in feet
    depth = 6  # Depth of the pool in feet
    volume = length * width * depth  # Volume of the pool in cubic feet
    required_chlorine = volume / 120  # Required amount of chlorine in quarts
    cost_per_quart = 3  # Cost of each quart of chlorine
    total_cost = required_chlorine * cost_per_quart  # Total cost of chlorine

    result = total_cost
    return result

print(solution())