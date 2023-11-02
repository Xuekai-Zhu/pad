def solution():
    """The average number of fruits per basket in five baskets is 25. If basket A contains 15 apples, B has 30 mangoes, C has 20 peaches, D has 25 pears and E has some bananas, how many bananas are in basket E?"""
    # Define the total number of fruits in the five baskets
    total_fruits = 25 * 5

    # Calculate the total number of fruits in baskets A, B, C, and D
    fruits_ABCD = 15 + 30 + 20 + 25

    # Calculate the number of bananas in basket E
    bananas_E = total_fruits - fruits_ABCD

    # Display the number of bananas in basket E
    result = bananas_E
    return result

print(solution())