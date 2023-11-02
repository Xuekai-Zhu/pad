def solution():
    # Calculate the profit made from selling one goldfish
    profit_per_goldfish = 0.75 - 0.25  # the store buys a goldfish for $0.25 and sells it for $0.75

    # Calculate the number of goldfish needed to make $100 in profit
    num_goldfish_needed = 100 / profit_per_goldfish

    # Calculate the actual profit made after one week of selling goldfish
    actual_profit = 0.55 * 100  # the owner is 45% short of the $100 price

    # Calculate the number of goldfish sold in one week
    num_goldfish_sold = actual_profit / profit_per_goldfish
    result = num_goldfish_sold
    return result

print(solution())