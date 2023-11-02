def solution():
    rack_cost = 2500  # Cost of the squat rack
    barbell_cost = rack_cost / 10  # Cost of the barbell (1/10 of the cost of the squat rack)

    # Calculate the total cost
    total_cost = rack_cost + barbell_cost
    result = total_cost
    return result

print(solution())