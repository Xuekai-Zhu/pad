def solution():
    """A plumber bought 10 meters of copper and 5 more meters of plastic pipe. If each meter cost $4, how much did the plumber spent on the copper and plastic pipe?"""
    copper_meters = 10
    plastic_meters = copper_meters + 5
    cost_per_meter = 4
    total_cost = (copper_meters + plastic_meters) * cost_per_meter
    result = total_cost
    return result

print(solution())