def solution():
    orange_price = 0.5
    total_fruits = 36
    total_bill = 66

    # Calculate the number of oranges bought
    num_oranges = total_fruits / 3

    # Calculate the number of apples and watermelons bought
    num_apple_or_watermelon = total_fruits / 3

    # Calculate the total cost of oranges
    total_orange_cost = num_oranges * orange_price

    # Calculate the cost of each apple or watermelon
    apple_or_watermelon_price = total_orange_cost / num_apple_or_watermelon

    # Calculate the cost of 1 apple
    apple_price = apple_or_watermelon_price / 4
    result = apple_price
    return result

print(solution())