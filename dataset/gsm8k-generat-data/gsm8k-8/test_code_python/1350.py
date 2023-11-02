def solution():
    # Calculate the total number of caterpillars
    total_caterpillars = 4 * 10

    # Calculate the number of caterpillars that become butterflies
    num_butterflies = int(total_caterpillars * 0.6)

    # Calculate the total money made from selling the butterflies
    total_money = num_butterflies * 3

    result = total_money
    return result

print(solution())