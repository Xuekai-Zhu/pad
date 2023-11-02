def solution():
    # Calculate the number of caterpillars that become butterflies
    num_caterpillars = 4 * 10  # 4 jars of 10 caterpillars each
    num_butterflies = num_caterpillars * 0.6  # 40% fail to become butterflies

    # Calculate the amount of money made from selling the butterflies
    money_made = num_butterflies * 3  # each butterfly is sold for $3
    result = money_made
    return result

print(solution())