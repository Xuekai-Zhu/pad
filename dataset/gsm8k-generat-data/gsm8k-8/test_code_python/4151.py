def solution():
    # Calculate the total weight of the cans
    can_weight = 2 * 20

    # Calculate the remaining weight for the bottles
    remaining_weight = 100 - can_weight

    # Calculate the number of bottles Jenny can carry
    num_bottles = remaining_weight // 6

    # Calculate the total amount of money Jenny makes
    total_money = num_bottles * 10 + 20 * 3

    result = total_money
    return result

print(solution())