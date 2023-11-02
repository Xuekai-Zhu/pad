def solution():
    # Calculate the total area of the ad spaces purchased by each company
    total_area_A = 10 * 12 * 5  # Company A purchased 10 ad spaces of size 12ft by 5ft
    total_area_B = 10 * 12 * 5  # Company B purchased 10 ad spaces of size 12ft by 5ft
    total_area_C = 10 * 12 * 5  # Company C purchased 10 ad spaces of size 12ft by 5ft
    total_area = total_area_A + total_area_B + total_area_C  # Total area of ad spaces purchased

    # Calculate the total cost of the ad spaces purchased
    cost_per_sq_ft = 60  # Each square foot ad was charged at $60
    total_cost = total_area * cost_per_sq_ft

    result = total_cost
    return result

print(solution())