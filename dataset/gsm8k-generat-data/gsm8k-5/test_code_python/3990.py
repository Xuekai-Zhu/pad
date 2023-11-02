def solution():
    num_plates = 100  # The charity is delivering 100 plates
    rice_cost = 0.10  # The cost of rice per plate is $0.10
    chicken_cost = 0.40  # The cost of chicken per plate is $0.40

    # Calculate the total cost for all plates
    total_cost = (num_plates * rice_cost) + (num_plates * chicken_cost)

    # Convert the total cost to dollars
    total_cost_dollars = total_cost / 100
    result = total_cost_dollars
    return result

print(solution())