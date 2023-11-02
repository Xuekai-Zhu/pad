def solution():
    """A bag of dozen apples costs $14 and Brian has already spent $10 on kiwis and half that much on bananas. What's the maximum number of apples Brian can buy if he left his house with only $50 and needs to pay the $3.50 subway fare each way?"""
    # Define the cost of a bag of dozen apples and the amount of money Brian has left after buying kiwis and bananas
    APPLE_COST = 14
    KIWI_COST = 10
    BANANA_COST = KIWI_COST / 2
    left_money = 50 - (2 * 3.5) - KIWI_COST - BANANA_COST

    # Calculate the maximum number of apples Brian can buy with the money left
    max_apples = left_money // APPLE_COST

    result = max_apples
    return result

print(solution())