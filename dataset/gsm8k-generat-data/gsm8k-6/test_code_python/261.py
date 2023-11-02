def solution():
    # Calculate the total cost of all fruits
    total_cost = 66  # total bill
    orange_cost = 0.5  # cost of one orange
    orange_count = 36/3  # evenly split between oranges, apples and watermelons
    orange_total_cost = orange_count * orange_cost
    apple_count = 36/3  # evenly split between oranges, apples and watermelons
    watermelon_count = 36/3  # evenly split between oranges, apples and watermelons
    apple_watermelon_total_cost = (apple_count/4 + watermelon_count) * orange_cost
    # Calculate the cost of one apple
    apple_cost = (total_cost - orange_total_cost - apple_watermelon_total_cost) / apple_count
    result = apple_cost
    return result

print(solution())