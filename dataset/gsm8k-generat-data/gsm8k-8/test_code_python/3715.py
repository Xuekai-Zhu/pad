def solution():
    # Find the total cost of buying a dozen boxes of highlighters
    total_cost = 12 * 10

    # Find the total number of highlighters bought
    total_highlighters = 12 * 30

    # Find the number of packages of six highlighters Sam makes
    num_packages = 5 * 30 // 6

    # Find the profit made from selling the packages of six highlighters
    package_profit = num_packages * (3 - (6/30)*10)

    # Find the number of highlighters sold separately
    num_separate_highlighters = total_highlighters - 5 * 30

    # Find the profit made from selling the highlighters separately
    separate_profit = (num_separate_highlighters // 3) * 2

    # Find the total profit made
    total_profit = package_profit + separate_profit - total_cost
    result = total_profit
    return result

print(solution())