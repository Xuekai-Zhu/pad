def solution():
    # Calculate the maximum number of bottles Jenny can carry
    max_bottles = (100 - (20 * 2)) // 6  # she can carry a total of 100 ounces and 20 cans, and each can weighs 2 ounces

    # Calculate the total weight of the bottles Jenny collected
    total_weight_bottles = max_bottles * 6

    # Calculate the total money Jenny makes
    total_money = (max_bottles * 10) + (20 * 3)  # she gets paid 10 cents per bottle and 3 cents per can

    result = total_money
    return result

print(solution())