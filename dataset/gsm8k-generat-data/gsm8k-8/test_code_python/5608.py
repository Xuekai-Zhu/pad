def solution():
    # Define the amount of profit made per watermelon
    profit_per_watermelon = 3

    # Calculate the total profit made
    total_profit = 105

    # Calculate the cost of the 18 watermelons sold
    cost_of_18_watermelons = 18 * profit_per_watermelon

    # Calculate the profit made from the watermelons not sold
    remaining_profit = total_profit - cost_of_18_watermelons

    # Calculate the number of watermelons originally had
    original_watermelons = remaining_profit / profit_per_watermelon
    result = original_watermelons
    return result

print(solution())