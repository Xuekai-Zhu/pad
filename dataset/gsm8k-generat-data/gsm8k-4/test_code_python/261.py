def solution():
    """You can buy 4 apples or 1 watermelon for the same price. You bought 36 fruits evenly split between oranges, apples and watermelons, and the price of 1 orange is $0.50. How much does 1 apple cost if your total bill was $66?"""
    # Define the number of oranges bought
    orange_count = 12

    # Define the total number of fruits bought
    fruit_count = 36

    # Define the total cost of the oranges
    orange_cost = orange_count * 0.5

    # Define the total cost of the bill
    total_cost = 66

    # Define the total cost of non-orange fruits
    non_orange_cost = total_cost - orange_cost

    # Define the number of watermelons bought
    watermelon_count = non_orange_cost // (4*1.0)

    # Define the number of apples bought
    apple_count = (non_orange_cost - (watermelon_count*4)) // (1*1.0)

    # Calculate the cost per apple
    apple_cost = non_orange_cost / apple_count

    result = round(apple_cost, 2)
    return result

print(solution())