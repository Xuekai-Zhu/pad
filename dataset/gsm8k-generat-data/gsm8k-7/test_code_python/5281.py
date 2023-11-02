def solution():
    husband_savings = 335 * 4 * 26/2 # 335 per week, 4 weeks in a month, 26 weeks in 6 months
    wife_savings = 225 * 4 * 26/2 # 225 per week, 4 weeks in a month, 26 weeks in 6 months
    total_savings = husband_savings + wife_savings

    # Divide half of the couple's savings equally among their four children
    num_children = 4
    each_child_savings = total_savings / 2 / num_children
    result = each_child_savings
    return result

print(solution())