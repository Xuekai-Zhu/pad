def solution():
    canvas_bag_carbon = 600
    plastic_bag_carbon = 4
    trips_per_canvas_bag = 8
    total_carbon_canvas_bag = canvas_bag_carbon * trips_per_canvas_bag
    total_carbon_plastic_bag = plastic_bag_carbon * trips_per_canvas_bag
    trips_lower_carbon_solution = total_carbon_canvas_bag / total_carbon_plastic_bag
    result = trips_lower_carbon_solution
    return result

print(solution())