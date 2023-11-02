def solution():
    total_quarters = 20  # Alice has 20 quarters
    total_nickels = total_quarters * 5  # She exchanges quarters for nickels
    iron_nickels = int(0.2 * total_nickels)  # 20% of the nickels are iron nickels
    regular_nickels = total_nickels - iron_nickels  # The rest are regular nickels

    # Calculate the total value of iron nickels and regular nickels
    iron_nickels_value = 3 * iron_nickels  # Iron nickels are worth $3 each
    regular_nickels_value = 0.05 * regular_nickels  # Regular nickels are worth 5 cents each

    # Calculate the total value of Alice's money now
    total_value = iron_nickels_value + regular_nickels_value + (total_quarters * 0.25)  # Add the value of her quarters

    result = total_value
    return result

print(solution())