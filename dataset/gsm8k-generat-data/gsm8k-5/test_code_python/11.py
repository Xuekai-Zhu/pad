def solution():
    # Total money saved from allowance
    allowance_savings = 5 * 3

    # Money earned from mowing lawns
    lawn_money = 15 * 4

    # Remaining money earned from shoveling driveways
    remaining_money = 95 - allowance_savings - lawn_money - 15

    # Calculate number of driveways shovelled
    driveways_shoveled = remaining_money // 7
    result = driveways_shoveled
    return result

print(solution())