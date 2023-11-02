def solution():
    # Determine the cost of one chocolate bar
    cost_of_one_magazine = 1
    cost_of_eight_magazines = 8 * cost_of_one_magazine
    cost_of_four_chocolates = cost_of_eight_magazines
    cost_of_one_chocolate = cost_of_four_chocolates / 4

    # Determine the cost of a dozen chocolate bars
    cost_of_dozen_chocolates = 12 * cost_of_one_chocolate
    result = cost_of_dozen_chocolates
    return result

print(solution())