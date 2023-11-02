def solution():
    can_weight = 2  # Each can weighs 2 ounces
    bottle_weight = 6  # Each bottle weighs 6 ounces
    max_weight = 100  # Jenny can carry a total of 100 ounces
    num_cans = 20  # Jenny collects 20 cans
    remaining_weight = max_weight - (num_cans * can_weight)  # Calculate the remaining weight for bottles

    # Calculate the maximum number of bottles Jenny can collect
    max_num_bottles = remaining_weight // bottle_weight

    # Calculate the total amount of money Jenny can make
    total_money = (max_num_bottles * 10) + (num_cans * 3)
    result = total_money
    return result

print(solution())