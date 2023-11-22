def solution():
    
    # Define the cost of the damage and the amount fine for road maintenance
    damage_cost = 450
    road_maintenance_fine = 120

    # Define the cost of each bucket of asphalt
    asphalt_cost = 25

    # Calculate the total cost of the asphalt
    asphalt_total_cost = asphalt_cost * 3

    # Calculate the total amount saved by fixing the pothole
    total_saved = damage_cost - road_maintenance_fine - asphalt_total_cost

    # return the result
    result = total_saved
    return result

print(solution())