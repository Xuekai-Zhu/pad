def solution():
    tire_repair_cost = 7  # Cost to repair each tire is $7
    sales_tax = 0.5  # Sales tax is 50 cents per tire
    num_tires = 4  # Juan needs all 4 tires repaired

    # Calculate the total cost for all 4 tires, including sales tax
    total_cost = (tire_repair_cost + sales_tax) * num_tires
    result = total_cost
    return result

print(solution())