def solution():
    """Mary wants to bake 10 apple pies for a charity event. Each pie needs 8 apples and she already harvested 50 apples from the trees in her garden. How many more apples does she need to buy to make all 10 pies?"""
    # Define the number of apples needed per pie and the number of apples already harvested
    APPLES_PER_PIE = 8
    HARVESTED_APPLES = 50

    # Calculate the total number of apples needed for all the pies
    total_apples_needed = APPLES_PER_PIE * 10

    # Calculate the number of apples that Mary still needs to buy
    apples_to_buy = total_apples_needed - HARVESTED_APPLES

    # Display the number of apples to buy
    result = apples_to_buy
    return result

print(solution())