def solution():
    quarters = 20
    nickels = 4 * quarters  # each quarter is exchanged for 5 nickels
    iron_nickels = 0.2 * nickels  # 20% of the nickels are iron nickels
    non_iron_nickels = nickels - iron_nickels  # remaining nickels are non-iron
    total_value = (non_iron_nickels * 5 + iron_nickels * 3) / 100  # total value in dollars
    result = total_value
    return result

print(solution())