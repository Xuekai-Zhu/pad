def solution():
    cost_of_magazine = 1
    num_chocolate_bars = 12

    # Calculate the cost of one chocolate bar
    cost_of_chocolate_bar = 8 * cost_of_magazine / 4

    # Calculate the cost of a dozen chocolate bars
    cost_of_dozen_chocolate_bars = num_chocolate_bars * cost_of_chocolate_bar
    result = cost_of_dozen_chocolate_bars
    return result

print(solution())