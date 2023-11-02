def solution():
    """A plumber bought 10 meters of copper and 5 more meters of plastic pipe. If each meter cost $4, how much did the plumber spent on the copper and plastic pipe?"""
    # Define the cost per meter of pipe
    COST_PER_METER = 4

    # Define the length of copper pipe purchased
    copper_pipe = 10

    # Define the length of plastic pipe purchased
    plastic_pipe = copper_pipe + 5

    # Calculate the total cost of copper pipe
    copper_cost = copper_pipe * COST_PER_METER

    # Calculate the total cost of plastic pipe
    plastic_cost = plastic_pipe * COST_PER_METER

    # Calculate the total cost of the purchase
    total_cost = copper_cost + plastic_cost

    # return the result
    result = total_cost
    return result

print(solution())