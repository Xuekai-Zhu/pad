def solution():
    """Mary wants to bake 10 apple pies for a charity event. Each pie needs 8 apples and she already harvested 50 apples from the trees in her garden. How many more apples does she need to buy to make all 10 pies?"""
    # Define the number of pies and the number of apples needed for each pie
    NUM_PIES = 10
    APPLES_PER_PIE = 8

    # Determine the total number of apples needed
    total_apples_needed = NUM_PIES * APPLES_PER_PIE

    # Determine the number of apples Mary already has
    apples_on_hand = 50

    # Determine how many more apples Mary needs to buy
    apples_needed = total_apples_needed - apples_on_hand

    # Return the result
    result = apples_needed
    return result

print(solution())