def solution():
    adult_haircut_cost = 48
    child_haircut_cost = 36
    tip_percentage = 20
    total_cost = (adult_haircut_cost * 2) + child_haircut_cost
    tip_amount = total_cost * (tip_percentage / 100)
    result = tip_amount
    return result

print(solution())