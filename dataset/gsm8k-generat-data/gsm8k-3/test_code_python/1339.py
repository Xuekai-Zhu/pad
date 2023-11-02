def solution():
    """A plumber bought 10 meters of copper and 5 more meters of plastic pipe. If each meter cost $4, how much did the plumber spent on the copper and plastic pipe?"""
    # Define the cost per meter of pipe
    COST_PER_METER = 4

    # Calculate the cost of the copper pipe
    copper_cost = 10 * COST_PER_METER

    # Calculate the length of the plastic pipe
    plastic_length = 10 + 5 # 5 more meters than the copper pipe
    # Calculate the cost of the plastic pipe
    plastic_cost = plastic_length * COST_PER_METER

    # Calculate the total cost of both types of pipe
    total_cost = copper_cost + plastic_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())