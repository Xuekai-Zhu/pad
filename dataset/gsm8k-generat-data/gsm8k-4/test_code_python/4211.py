def solution():
    """The average number of fruits per basket in five baskets is 25. If basket A contains 15 apples, B has 30 mangoes, C has 20 peaches, D has 25 pears and E has some bananas, how many bananas are in basket E?"""
    # Define the total number of fruits and baskets
    total_fruits = 5 * 25
    total_baskets = 5

    # Calculate the number of fruits in baskets A, B, C, and D
    fruits_A = 15
    fruits_B = 30
    fruits_C = 20
    fruits_D = 25

    # Calculate the number of fruits in basket E
    fruits_E = total_fruits - fruits_A - fruits_B - fruits_C - fruits_D

    # Return the number of bananas in basket E
    result = fruits_E
    return result

print(solution())