def solution():
    """John gave his fiancee a $4000 ring on their engagement day, a $2000 car as a gift on their wedding day, and a diamond brace twice as expensive as the ring he gave her during the engagement. What's the worth of the presents John gave to her fiancee?"""
    # Define the cost of the ring, car and diamond bracelet
    RING_COST = 4000
    CAR_COST = 2000
    DIAMOND_BRACELET_COST = 2 * RING_COST

    # Calculate the total worth of the presents
    total_worth = RING_COST + CAR_COST + DIAMOND_BRACELET_COST

    # Display the total worth
    result = total_worth
    return result

print(solution())