def solution():
    fabric_monday = 20
    fabric_tuesday = fabric_monday * 2
    fabric_wednesday = fabric_tuesday / 4

    cost_fabric = fabric_monday + fabric_tuesday + fabric_wednesday
    cost_yarn = 0  # assume no yarn is delivered
    total_cost = (cost_fabric * 2) + (cost_yarn * 3)
    result = total_cost
    return result

print(solution())