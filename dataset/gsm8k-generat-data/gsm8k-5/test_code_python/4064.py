def solution():
    cost_of_8_magazines = 4 * cost_of_1_chocolate_bars  # Four chocolate bars costs the same as 8 magazines
    cost_of_1_magazine = 1  # Each magazine costs $1
    cost_of_1_chocolate_bars = cost_of_8_magazines / 8  # Calculate the cost of one chocolate bar

    # Calculate the cost of a dozen chocolate bars
    dozen_chocolate_bars = 12 * cost_of_1_chocolate_bars
    result = dozen_chocolate_bars
    return result

print(solution())