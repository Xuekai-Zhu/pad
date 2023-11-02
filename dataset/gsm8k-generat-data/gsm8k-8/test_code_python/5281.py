def solution():
    # Calculate the total savings after 6 months
    husband_savings = 335 * 4 * 26
    wife_savings = 225 * 4 * 26
    total_savings = husband_savings + wife_savings

    # Calculate half of the total savings
    half_savings = total_savings / 2

    # Divide the half savings equally between the 4 children
    each_child_share = half_savings / 4

    result = each_child_share
    return result

print(solution())