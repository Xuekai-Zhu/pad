def solution():
    """A bag of dozen apples costs $14 and Brian has already spent $10 on kiwis and half that much on bananas. What's the maximum number of apples Brian can buy if he left his house with only $50 and needs to pay the $3.50 subway fare each way?"""
    # Define the cost of a bag of a dozen apples, the amount spent on kiwis and bananas, and the cost of the subway fare
    APPLE_COST = 14
    KIWI_COST = 10
    BANANA_COST = KIWI_COST / 2
    SUBWAY_FARE = 3.5

    # Define the maximum amount Brian can spend on apples after accounting for his other expenses and the subway fare
    MAX_APPLE_COST = 50 - KIWI_COST - (BANANA_COST / 2) - (SUBWAY_FARE * 2)

    # Calculate the maximum number of bags of apples Brian can buy
    max_bags = MAX_APPLE_COST / APPLE_COST

    # Calculate the maximum number of apples Brian can buy
    max_apples = max_bags * 12

    # Display the maximum number of apples Brian can buy
    result = max_apples
    return result

print(solution())