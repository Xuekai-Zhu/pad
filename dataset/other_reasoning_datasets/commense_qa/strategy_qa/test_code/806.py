def solution():
    hilux_capacity = 7700
    studd_weight = 364
    num_studd_clones = 30
    total_weight = studd_weight * num_studd_clones
    if total_weight <= hilux_capacity:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())