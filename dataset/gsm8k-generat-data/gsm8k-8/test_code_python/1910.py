def solution():
    # Calculate Johnson's yield per hectare per month
    johnson_yield = 80 / 2 # 40

    # Calculate the neighbor's yield per hectare per month
    neighbor_yield = 2 * johnson_yield * 2 # 160

    # Calculate Johnson's total yield for 6 months
    johnson_total_yield = johnson_yield * 6 # 240

    # Calculate the neighbor's total yield for 6 months
    neighbor_total_yield = neighbor_yield * 2 * 6 # 1920

    # Calculate the total yield for both fields
    total_yield = johnson_total_yield + neighbor_total_yield

    result = total_yield
    return result

print(solution())