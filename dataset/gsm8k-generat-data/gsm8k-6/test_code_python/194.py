def solution():
    # Calculate the total cost before rebate
    cost_before_rebate = (3 * 26) + (2 * 83) + 90

    # Subtract the rebate from the total cost
    cost_after_rebate = cost_before_rebate - 12
    result = cost_after_rebate
    return result

print(solution())