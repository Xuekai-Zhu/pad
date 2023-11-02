def solution():
    # Calculate the total area of fabric needed for the overskirt and petticoats
    area_skirts = 3 * (12 * 4)  # Three skirts, each using a 12 by 4 rectangle of fabric

    # Calculate the total area of fabric needed for the bodice
    area_bodice = 2 + (2 * 5)  # 2 sq. ft. for the shirt and 5 sq. ft. for each sleeve

    # Calculate the total area of fabric needed for the entire costume
    total_area = area_skirts + area_bodice

    # Calculate the total cost of the fabric
    cost_per_sq_ft = 3  # $3 per sq. ft. of fabric
    total_cost = total_area * cost_per_sq_ft
    result = total_cost
    return result

print(solution())