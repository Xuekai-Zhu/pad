def solution():
    roof_weight_limit = 500
    leaves_per_day = 100
    weight_per_thousand_leaves = 1

    # Calculate the total weight of leaves that fall on Bill's roof each day
    total_weight_per_day = (leaves_per_day / 1000) * weight_per_thousand_leaves

    # Calculate the number of days it will take for the roof to reach its weight limit
    days_to_collapse = roof_weight_limit / total_weight_per_day
    result = days_to_collapse
    return result

print(solution())