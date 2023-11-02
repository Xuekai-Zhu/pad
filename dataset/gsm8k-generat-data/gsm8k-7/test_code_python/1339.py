def solution():
    copper_length = 10
    plastic_length = copper_length + 5  # 5 more meters of plastic pipe
    cost_per_meter = 4

    # Calculate the total cost of copper
    copper_cost = copper_length * cost_per_meter

    # Calculate the total cost of plastic pipe
    plastic_cost = plastic_length * cost_per_meter

    # Calculate the total cost of both copper and plastic pipe
    total_cost = copper_cost + plastic_cost
    result = total_cost
    return result

print(solution())