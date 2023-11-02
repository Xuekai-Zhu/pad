def solution():
    """Tammy just got her hair cut. For every 14 haircuts, she gets a free additional haircut. She has gotten 5 free haircuts already. She is 5 haircuts away from another free one. How many haircuts has she gotten there?"""
    # Define the number of free haircuts Tammy has already received
    FREE_HAIRCUTS = 5

    # Define the number of haircuts required for another free one
    HAIRCUTS_FOR_FREE = 14 - 5

    # Define the number of haircuts Tammy has received
    haircuts = FREE_HAIRCUTS * HAIRCUTS_FOR_FREE + 5

    # Display the total number of haircuts Tammy has received
    result = haircuts
    return result

print(solution())