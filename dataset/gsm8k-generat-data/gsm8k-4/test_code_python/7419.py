def solution():
    """Tapanga and Corey have 66 candies together. However, Tapanga has 8 more candies than Corey. How many candies does Corey have?"""
    # Define the total number of candies and the difference in candies between Tapanga and Corey
    total_candies = 66
    candy_difference = 8

    # Calculate Corey's number of candies using algebraic equations
    # Let x be Corey's number of candies
    # Then Tapanga's number of candies is x + candy_difference
    # The sum of their candies is total_candies, so we can write an equation:
    # x + (x + candy_difference) = total_candies
    # Simplifying:
    # 2x + candy_difference = total_candies
    # x = (total_candies - candy_difference) / 2

    corey_candies = (total_candies - candy_difference) / 2

    result = corey_candies
    return result

print(solution())