def solution():
    brother_weight = 2 * felix_weight
    brother_lift = 3 * brother_weight
    felix_lift_weight_ratio = 1.5
    felix_lift = felix_lift_weight_ratio * felix_weight

    felix_lift_per_pound = felix_lift / felix_weight
    felix_lift_total = felix_lift_per_pound * brother_lift

    result = felix_lift_total
    return result

print(solution())