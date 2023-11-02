def solution():
    num_plates = 100
    rice_cost_per_plate = 0.10
    chicken_cost_per_plate = 0.40

    # Calculate the total cost of all rice plates
    total_rice_cost = num_plates * rice_cost_per_plate

    # Calculate the total cost of all chicken plates
    total_chicken_cost = num_plates * chicken_cost_per_plate

    # Calculate the total cost of all food for the dinners
    total_cost = total_rice_cost + total_chicken_cost
    result = total_cost
    return result

print(solution())