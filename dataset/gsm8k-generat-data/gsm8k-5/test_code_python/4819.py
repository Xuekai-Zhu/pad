def solution():
    # Calculate the total amount contributed by the boss and Todd
    total_contributed = 15 + (2 * 15)  # Todd contributes twice as much as the boss

    # Calculate the remaining amount needed from the remaining 5 employees
    remaining_amount = 100 - total_contributed

    # Calculate the amount each of the remaining 5 employees need to pay
    each_pays = remaining_amount / 5
    result = each_pays
    return result

print(solution())