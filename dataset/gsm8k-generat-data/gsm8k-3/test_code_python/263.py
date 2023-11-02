def solution():
    """You can buy 4 apples or 1 watermelon for the same price. You bought 36 fruits evenly split between oranges, apples and watermelons, and the price of 1 orange is $0.50. How much does 1 apple cost if your total bill was $66?"""
    # Define the price of an orange and the number of fruits of each type purchased
    ORANGE_PRICE = 0.5
    ORANGES = 12
    APPLES = 12
    WATERMELONS = 12

    # Calculate the total cost of the oranges
    orange_cost = ORANGES * ORANGE_PRICE

    # Calculate the total cost of the watermelons
    watermelon_cost = 4 * ORANGE_PRICE * (WATERMELONS // 4)

    # Calculate the total cost of the apples
    apple_cost = (66 - orange_cost - watermelon_cost) / APPLES

    # Display the cost of one apple
    result = apple_cost
    return result

print(solution())