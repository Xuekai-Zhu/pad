def solution():
    tire_repair_cost = 7
    sales_tax = 0.50
    num_tires = 4

    # Calculate the total cost of repairing all tires, including sales tax
    total_cost = (tire_repair_cost + sales_tax) * num_tires
    result = total_cost
    return result

print(solution())