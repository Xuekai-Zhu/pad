def solution():
    """Tammy just got her hair cut. For every 14 haircuts, she gets a free additional haircut. She has gotten 5 free haircuts already. She is 5 haircuts away from another free one. How many haircuts has she gotten there?"""
    # Define the number of haircuts needed to get a free one
    FREE_HAIRCUTS = 14

    # Define the number of free haircuts already received
    free_haircuts_received = 5

    # Define the number of haircuts until the next free one
    haircuts_until_free = 5

    # Calculate the total number of haircuts received, including the free ones
    total_haircuts_received = (free_haircuts_received + 1) * FREE_HAIRCUTS - haircuts_until_free

    # return the result
    result = total_haircuts_received
    return result

print(solution())